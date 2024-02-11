from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('aanmelden', views.aanmelden, name='aanmelden'),
    path('uitloggen', views.uitloggen, name='uitloggen'),
    path('post_list', views.post_list, name='post_list'), 
]