# URL config for posts app  
# Flow: urls.py -> views.py -> templates

from django.contrib import admin
from django.urls import path
from posts import views as views

urlpatterns = [
    # Home page url
    path('', views.home, name='home'),
    # Recipe posts page url
    path('recipeposts', views.recipeposts, name='recipeposts')
    
]
