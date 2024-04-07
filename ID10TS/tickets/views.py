from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Ticket


# The page that anyone can see prior to logging in
def index(request):
    latest_ticket_list = Ticket.objects.order_by("-date_opened")[:5]
    context = {"latest_ticket_list": latest_ticket_list}
    return render(request, "tickets/index.html", context)


# View the ticket as a regular user
def detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    comments = ticket.comment_set.all().order_by('-date_opened')
    context = {"ticket": ticket, "comments": comments}
    return render(request, "tickets/detail.html", context)


# View the ticket as an admin with more privileges
def privileged(request, ticket_id):
    pass


# The page that you see prior to (or after) making a ticket
def home(request):
    pass
