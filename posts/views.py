from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

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
@login_required
def recipeposts(request):
    recipes = RecipePost.objects.filter(created_by=request.user).order_by('-created_on') 
    recipescount = recipes.count()
    context = {
        'recipes': recipes,
        'recipescount': recipescount
        }
    return render(request, 'posts/recipeposts.html', context)

# Create page view
@login_required
def create(request):
    form = RecipePostForm()
    # Handle form submission --> POST request 
    if request.method == 'POST':
        form = RecipePostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            category = form.cleaned_data['category']
            tags = form.cleaned_data['tags']

            # Create a new recipe post object and save it to the database
            recipe = RecipePost(
                title=title, 
                content=content,
                image=image,
                category=category, 
                created_by=request.user
            )
            recipe.save()
            recipe.tags.set(tags) # Set the many-to-many relationship for tags

            # After submitting the form, redirect the user to the recipe posts page
            return redirect('recipeposts')
    context = {'form': form}
    return render(request, 'posts/create.html', context)

# Edit page view
@login_required
def edit(request, pk):
    recipe = RecipePost.objects.get(id=pk) # Get the recipe post object with the given id and created by the current user)
    if request.user != recipe.created_by:
        return redirect('home')
    form = RecipePostForm(instance=recipe)
    if request.method == 'POST':
        form = RecipePostForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'posts/edit.html', context)

# Delete page view
@login_required
def delete(request, pk):
    recipe = RecipePost.objects.get(id=pk) # Get the recipe post object with the given id and created by the current user)
    if request.user != recipe.created_by:
        return redirect('home')
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    context = {'recipe': recipe}
    return render(request, 'posts/delete.html', context)

# Details page view
def details(request, pk):
    recipe = RecipePost.objects.get(id=pk)
    context = {'recipe': recipe}
    return render(request, 'posts/details.html', context)