from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'service_category', 'date_time', 'urgency', 'users_impacted', 'description']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'service_category': 'Service Category',
            'date_time': 'Date/Time',
            'urgency': 'Urgency',
            'users_impacted': 'Users Impacted'
        }
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'service_category': forms.Select(choices=[
                ('MS Office', 'MS Office'),
                ('Printer', 'Printer'),
                ('Network', 'Network'),
                # Add more choices as needed
            ]),
            'urgency': forms.Select(choices=[
                ('Low', 'Low'),
                ('Medium', 'Medium'),
                ('High', 'High'),
            ])
        }


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']