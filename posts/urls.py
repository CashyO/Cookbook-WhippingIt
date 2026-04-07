# URL config for posts app  
# Flow: urls.py -> views.py -> templates

from django.contrib import admin
from django.urls import path
from posts import views as views

urlpatterns = [
    # Home page url
    path('', views.home, name='home'),
    # Recipe posts page url
    path('recipeposts', views.recipeposts, name='recipeposts'),
    # Create page url
    path('create', views.create, name='create'), 
    # Edit page url
    path('edit/<int:pk>', views.edit, name='edit'),
    # Delete page url   
    path('delete/<int:pk>', views.delete, name='delete'),
    # Details page url   
    path('details/<int:pk>', views.details, name='details')
]
