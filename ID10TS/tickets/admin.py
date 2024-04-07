from django.contrib import admin

from .models import Comment, Ticket, TicketCategory

admin.site.register(Ticket)
admin.site.register(TicketCategory)
admin.site.register(Comment)