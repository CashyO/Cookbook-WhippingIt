from django.shortcuts import redirect, render
from .forms import *
from .models import *

# Create your views here.
# Flow: urls.py -> views.py -> templates

# Home page view
def home(request):
    # Retrieve all recipe posts from the database (.filter() can be used to filter the results based on certain criteria) 
    recipes = RecipePost.objects.all().order_by('-created_on') 
    recipescount = recipes.count()
    context = {
        'recipes': recipes,
        'recipescount': recipescount
        }
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

def edit(request, pk):
    recipe = RecipePost.objects.get(id=pk)
    form = RecipePostForm(instance=recipe)
    if request.method == 'POST':
        form = RecipePostForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'posts/edit.html', context)

def delete(request, pk):
    recipe = RecipePost.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    context = {'recipe': recipe}
    return render(request, 'posts/delete.html', context)