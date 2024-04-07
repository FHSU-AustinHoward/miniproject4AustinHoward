# INF601 - Advanced Programming in Python
# Austin Howard
# Mini Project 4

from django import forms
from .models import Comment


# Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']