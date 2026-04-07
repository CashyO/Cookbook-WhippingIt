from django.shortcuts import render

# Create your views here.
# Flow: urls.py -> views.py -> templates

# Home page view
def home(request):
    title = "this is my title"
    context = {'title': title}
    return render(request, 'posts/home.html', context)

# Recipe posts page view
def recipeposts(request):
    context = {}
    return render(request, 'posts/recipeposts.html', context)

