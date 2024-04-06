from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LoginForm, RegistrationForm
from .forms import TicketForm

from .models import Ticket

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or any other page
    else:
        form = TicketForm()
    return render(request, 'ID10T/create_ticket.html', {'form': form})

@login_required
def admin_dashboard(request):
    # Retrieve all tickets from the database
    tickets = Ticket.objects.all()

    # Pass the tickets to the template
    return render(request, 'ID10T/admin_dashboard.html', {'tickets': tickets})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    # Redirect to admin dashboard if the user is an admin
                    return redirect('admin_dashboard')
                else:
                    # Redirect to the homepage for regular users
                    return redirect('home')  # Replace 'home' with the URL name for the homepage
            else:
                return render(request, 'ID10T/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'ID10T/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print("Registration successful. Redirecting to login page.")
            return HttpResponseRedirect('/login/')  # Redirect to the login page
        else:
            print("Form is not valid. Errors:", form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'ID10T/register.html', {'form': form})


