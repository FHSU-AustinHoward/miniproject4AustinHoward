from django.contrib import admin

from .models import Ticket, TicketCategory

admin.site.register(Ticket)
admin.site.register(TicketCategory)