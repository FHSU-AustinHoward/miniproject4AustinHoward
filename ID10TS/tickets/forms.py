# INF601 - Advanced Programming in Python
# Austin Howard
# Mini Project 4

from django import forms
from .models import Comment


# Ticket Form
from django import forms
from .models import Ticket


# Ticket Form
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'ticket_category', 'priority', 'users_impacted', 'description', 'assigned_to']

    def clean(self):
        cleaned_data = super().clean()
        users_impacted = cleaned_data.get('users_impacted')
        if users_impacted and users_impacted < 1:
            raise forms.ValidationError("Number of users impacted must be at least 1.")
        return cleaned_data


# Comments form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
