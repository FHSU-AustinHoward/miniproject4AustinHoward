# INF601 - Advanced Programming in Python
# Austin Howard
# Mini Project 4

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Vulnerability, Reporter, AffectedSystem


@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_vulnerabilities = Vulnerability.objects.all().count()
    num_systems = AffectedSystem.objects.all().count()
    num_reporters = Reporter.objects.all().count()

    # Context data
    context = {
        'num_vulnerabilities': num_vulnerabilities,
        'num_systems': num_systems,
        'num_reporters': num_reporters,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class VulnerabilityListView(LoginRequiredMixin, ListView):
    # This view allows a logged-in user to view the vulnerability list

    # Variables
    model = Vulnerability
    template_name = 'vulnerability_list.html'
    context_object_name = 'vulnerability_list'
    paginate_by = 20

    # Context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paginated'] = self.paginate_by is not None
        return context


class VulnerabilityDetailView(LoginRequiredMixin, DetailView):
    # This view shows detailed information fore the selected vulnerability
    model = Vulnerability
    template_name = 'vulnerability_detail.html'
    context_object_name = 'vulnerability_detail'


class SystemsListView(LoginRequiredMixin, ListView):
    # This view allows a logged-in user to view the affected system list

    # Variables
    model = AffectedSystem
    template_name = 'system_list.html'
    context_object_name = 'system_list'
    paginate_by = 20

    # Context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paginated'] = self.paginate_by is not None
        return context


class SystemDetailView(LoginRequiredMixin, DetailView):
    # This view shows detailed information for the selected vulnerability
    model = AffectedSystem
    template_name = 'system_detail.html'
    context_object_name = 'system_detail'
