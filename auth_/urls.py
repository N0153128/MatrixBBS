from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'Auth_'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.out, name='logout'),
]
