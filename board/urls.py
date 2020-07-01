from django.urls import path
from . import views

app_name = 'Board'
urlpatterns = [
    path('', views.Board, name='board'),
    path('<int:pk>', views.threadview, name='thread'),

]
