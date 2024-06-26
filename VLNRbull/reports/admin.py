# INF601 - Advanced Programming in Python
# Austin Howard
# Mini Project 4

from django.contrib import admin
from .models import Reporter, Vulnerability, AffectedSystem


class VulnerabilityAdmin(admin.ModelAdmin):
    # Display data as a fieldset with groups instead of a list view
    fieldsets = [
        ('Report Information', {
            'fields':['severity', 'status', 'reporter']
        }),
        ('Vulnerability Information', {
            'fields': ['title', 'description'],
        }),
        ('Additional Information', {
            'fields': ['date_opened','affected_systems'],
        }),
    ]
    # Date opened should never be modified
    readonly_fields = ['date_opened']


class ReporterAdmin(admin.ModelAdmin):
    pass


class AffectedSystemAdmin(admin.ModelAdmin):
    # Display fields as a list and enable search for the list
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


# Register the admin class with the associated model
admin.site.register(Vulnerability, VulnerabilityAdmin)
admin.site.register(AffectedSystem, AffectedSystemAdmin)
admin.site.register(Reporter, ReporterAdmin)