from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create a class for the Post database model 

# Change these later 

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class RecipePost(models.Model): # Create table 
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title # used to identify the record
    
# Class for comments on recipe posts 
class Comment(models.Model):
    recipe = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name='comments')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.created_by.username} on {self.recipe.title}'