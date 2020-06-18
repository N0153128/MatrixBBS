from django.urls import path
from . import views

app_name = 'Board'
urlpatterns = [
    path('greetings/', views.main, name='greetings'),
    path('board/', views.Board, name='board'),
    path('board/<int:pk>', views.threadview, name='thread'),
    path('board/<int:pk>', views.CommentsView.as_view(), name='comment'),

]
