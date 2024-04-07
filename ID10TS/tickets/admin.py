from django.contrib import admin

from .models import Comment, Ticket, TicketCategory


class TicketAdmin(admin.ModelAdmin):
    list_display = ["title", "date_opened"]
    list_filter = ["date_opened"]
    search_fields = ["title"]
    fieldsets = [
        ('Ticket Information', {'fields': ['title']}),
        ("Date information", {"fields": ["date_opened"]}),
    ]


admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketCategory)
admin.site.register(Comment)