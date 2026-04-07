from django.shortcuts import redirect, render
from .forms import *
from .models import *

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

# Create page view
def create(request):
    form = RecipePostForm()
    # Handle form submission --> POST request 
    if request.method == 'POST':
        form = RecipePostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            # Create a new recipe post object and save it to the database
            recipe = RecipePost(
                title=title, 
                content=content
            )
            recipe.save()

            # After submitting the form, redirect the user to the recipe posts page
            return redirect('recipeposts')
    context = {'form': form}
    return render(request, 'posts/create.html', context)
