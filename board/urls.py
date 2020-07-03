from django.urls import path
from . import views
from .views import *

app_name = 'Board'
urlpatterns = [
    path('', views.Board, name='board'),
    path('<int:pk>', views.threadview, name='thread'),
    path('<int:pk>/delete/', views.ThreadDelete.as_view(), name='delete_thread'),

]
