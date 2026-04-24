from django.contrib import admin
# Import the models.py tables
from .models import * 

# Register your models here.

admin.site.register(RecipePost)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)