from django import forms
from django.core.exceptions import ValidationError

from .models import *


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
