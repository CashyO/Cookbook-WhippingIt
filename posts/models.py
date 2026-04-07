from django.db import models

# Create your models here.

# Create a class for the Post database model 

# Change these later 
class RecipePost(models.Model): # Create table 
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title # used to identify the record
    
