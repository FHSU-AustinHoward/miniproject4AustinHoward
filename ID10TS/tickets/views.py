# INF601 - Advanced Programming in Python
# Austin Howard
# Mini Project 4

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import CommentForm, TicketForm
from .models import Ticket


class IndexView(generic.ListView):
    template_name = "tickets/index.html"
    context_object_name = "tickets"  # Update context object name
    queryset = Ticket.objects.order_by("-date_opened")[:5]  # Alternatively, you can use queryset attribute directly



class CreateTicketView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = "tickets/create_ticket.html"

    def form_valid(self, form):
        # Save the form
        ticket = form.save()

        # Redirect to the detail view of the newly created ticket
        return HttpResponseRedirect(reverse('tickets:detail', kwargs={'pk': ticket.pk}))


class DetailView(generic.DetailView):
    model = Ticket
    template_name = "tickets/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket = self.get_object()
        comments = ticket.comment_set.all().order_by('-date_opened')
        context['comments'] = comments
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        ticket = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.save()
            return HttpResponseRedirect(reverse('tickets:detail', kwargs={'pk': ticket.pk}))
        else:
            # Handle invalid form submission
            # You may want to provide feedback to the user here
            pass


class PrivilegedView(generic.DetailView):
    model = Ticket
    template_name = "tickets/privileged.html"

    def post(self, request, *args, **kwargs):
        ticket = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.save()
            return HttpResponseRedirect(reverse('tickets:privileged', args=(ticket.id,)))
        else:
            # Handle invalid form submission
            # You may want to provide feedback to the user here
            pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket = self.get_object()
        comments = ticket.comment_set.all().order_by('-date_opened')
        context['comments'] = comments
        context['form'] = CommentForm()
        return context

