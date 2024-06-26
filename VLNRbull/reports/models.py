# INF601 - Advanced Programming in Python
# Austin Howard
# Mini Project 4

from django.db import models
from django.urls import reverse


class Reporter(models.Model):
    # This Model describes who submitted the report.
    # This is not necessarily a username, could be external an external source

    # Fields
    username = models.CharField(
        max_length=30,
        help_text='Enter a username',
        unique=True
    )
    email = models.EmailField(
        primary_key=True,
        help_text='Enter your email address'
    )

    # Metadata
    class Meta:
        ordering = ['username']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('reporter-detail-view', args=[self.username])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.username


class Vulnerability(models.Model):
    # This model describes the nature of the vulnerability.
    # In addition, it has variables that assists admins in prioritization

    # Variable Lists
    SEVERITY_CHOICES = [
        # Describes the priority of the report.
        # This is from the point of view of the administrator.
        ('1', "Low"),
        ('2', "Medium"),
        ('3', "High"),
        # Modify further if needed
    ]

    STATUS_CHOICES = [
        # Describes the state of the report
        ('1', "Open"),
        ('2', "Testing"),
        ('3', "Closed"),
        # Modify further if needed
    ]

    # Fields
    title = models.CharField(
        max_length = 30,
        help_text='Enter title of vulnerability.'
    )
    description = models.TextField(
        max_length = 500,
        help_text='Describe the vulnerability, impact, and troubleshooting'
    )
    severity = models.CharField(
        max_length = 6,
        choices = SEVERITY_CHOICES,
        default='1'
    )
    date_opened = models.DateTimeField(
        'date opened',
        auto_now_add=True
    )
    status = models.CharField(
        max_length = 9,
        choices = STATUS_CHOICES,
        default='1'
    )
    reporter = models.ForeignKey(
        Reporter,
        on_delete=models.CASCADE,
        related_name='vulnerabilities'
    )
    affected_systems = models.ManyToManyField(
        'AffectedSystem',
        related_name='related_vulnerabilities'
    )

    # Metadata
    class Meta:
        # Sorts the chart in the admin view by date opened (not id)
        ordering = ['date_opened']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('vulnerability-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title


class AffectedSystem(models.Model):
    # This model describes the system affected by the vulnerability.

    # Fields
    name = models.CharField(
        max_length=50,
        help_text='Enter the name of the affected system'
    )
    description = models.TextField(
        max_length=500,
        help_text='Describe the purpose of the affected system'
    )
    vulnerabilities = models.ManyToManyField(
        'Vulnerability',
        related_name='related_affected_systems'
    )

    # Metadata
    class Meta:
        # Sorts the chart in the admin view by name (not id)
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('system-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name
