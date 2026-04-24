from django.shortcuts import redirect, render
from django.db.models import Q
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
# Flow: urls.py -> views.py -> templates

# Home page view
def home(request):
    # Get the search query from the request
    q = request.GET.get('q', '').strip()
    selected_category = request.GET.get('category', '').strip()

    # Retrieve all recipe posts from the database (.filter() can be used to filter the results based on certain criteria) 
    recipes = RecipePost.objects.all().order_by('-created_on') 
    categories = Category.objects.all().order_by('name')

    # Filter the recipe posts based on the search query and selected category
    if q: 
        recipes = recipes.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q) |
            Q(category__name__icontains=q) |
            Q(tags__name__icontains=q) |
            Q(created_by__username__icontains=q)
        ).distinct()
    if selected_category:
        recipes = recipes.filter(
            category__name=selected_category
        )

    recipescount = recipes.count()

    context = {
        'recipes': recipes,
        'recipescount': recipescount,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': q,
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
    comments = recipe.comments.all()
    comment_form = CommentForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.recipe = recipe
                comment.created_by = request.user
                comment.save()

                return redirect('details', pk=recipe.id)
        else:
            return redirect('login')

    context = {
        'recipe': recipe,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'posts/details.html', context)

# Comment delete view
@login_required
def delete_comment(request, pk):
    # Get the comment object with the given id
    comment = Comment.objects.get(id=pk)
    recipe_id = comment.recipe.id

    # Check if the user is the creator of the comment before allowing deletion
    if request.user != comment.created_by:
        return redirect('details', pk=recipe_id)

    # Handle the POST request to delete the comment
    if request.method == 'POST':
        comment.delete()
        return redirect('details', pk=recipe_id)

    return redirect('details', pk=recipe_id)