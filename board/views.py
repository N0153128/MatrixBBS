from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Thread, Comment
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ThreadForm, CommentForm


def main(request):
    return render(request, 'main.html')


@method_decorator(login_required, name='dispatch')
class CommentsView(generic.DetailView):
    model = Comment
    template_name = 'board/comments.html'


@login_required
def Board(request):
    #thread = get_object_or_404(Thread)
    latest_thread = Thread.objects.order_by('-pub_date')[:10]
    template = loader.get_template('board/board.html')

    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            former = form.save(commit=False)
            former.category = form.cleaned_data['category']
            former.thread_author = request.user
            former.save()
            return HttpResponseRedirect(reverse('Board:board'))
        else:
            raise Http404("Something went wrong")
    form = ThreadForm()
    context = {
        'latest_threads': latest_thread,
        'form': form,
    }
    return HttpResponse(template.render(context,request))



class ThreadDelete(DeleteView):
    model = Thread
    success_url = reverse_lazy('Board:board')


@login_required
def threadview(request, pk):
    thread = Thread.objects.get(id = pk)
    comments = Comment.objects.filter(comment_post = thread)
    template = loader.get_template('board/thread.html')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            former = form.save(commit=False)
            former.comment_text = form.cleaned_data['comment_text']
            former.comment_author = request.user
            former.comment_post = thread
            former.save()
            return HttpResponseRedirect(reverse('Board:thread', kwargs={'pk':thread.id}))
        else:
            raise Http404("Something went wrong")

    form = CommentForm()
    context = {
        'thread': thread,
        'form': form,
        'comments': comments
    }
    return HttpResponse(template.render(context, request))
