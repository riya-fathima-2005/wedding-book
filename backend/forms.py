from django import forms
from .models import Blog
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Page

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


    


class PageForm(forms.ModelForm):

    content = forms.CharField(
        widget=CKEditor5Widget(
            config_name="extends"
        )
    )

    class Meta:
        model = Page
        fields = "__all__"