from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'category',
            'title',
            'image',
            'short_description',
            'content',
            'author',
            'meta_title',
            'meta_description',
            'meta_keywords',
            'is_published'
        ]