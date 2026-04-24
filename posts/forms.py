from django import forms
from .models import *

class RecipePostForm(forms.ModelForm):
    # create forms for the recipepost model in models.py 
    title = forms.CharField(
        label = "Recipe Title",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter the title of your recipe'})
    )
    content = forms.CharField(
        label= "Recipe Content",
        widget=forms.Textarea(attrs={'placeholder': 'Enter the content of your recipe', 'rows': 8})
    )
    image = forms.ImageField(
        label= "Upload Recipe Image",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label="Select Category",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        label="Select Tags",
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    # Meta class to specify the model and fields to be used in the form
    class Meta:
        model= RecipePost
        fields = ['title', 'content', 'image', 'category', 'tags']

# Create a form for the comment model in models.py
class CommentForm(forms.ModelForm):
    body = forms.CharField(label="Leave a Comment", widget=forms.Textarea(attrs={
                                'placeholder': 'Write your comment here...',
                                'rows': 4,
                                'class': 'form-control'
                            })
                        )

    class Meta:
        model = Comment
        fields = ['body']
