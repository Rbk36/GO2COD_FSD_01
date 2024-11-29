from django import forms
from .models import Post

class PostForm(forms.ModelsForm):
    class meta:
        model=Post
        fields='__all__'
        
        widget={
            
            
            
        }