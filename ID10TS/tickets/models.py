# INF601 - Advanced Programming in Python
# Austin Howard
# Mini Project 4

import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class TicketCategory(models.Model):
    # Allows a more flexible way to add categories rather than a preset list
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        # Use the name of the ticket category when class is called as a string
        return self.name

    class Meta:
        # Displays "Categories" instead of "Categorys"
        verbose_name_plural = "Categories"


class Ticket(models.Model):
    # Status descriptions of the ticket to indicate progress
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Closed', 'Closed'),
        ('InProgress', 'In Progress'),
        ('OnHold','On Hold')
        # Add more choices as needed
    ]

    # Priority of the ticket from the standpoint of administrators
    PRIORITY_CHOICES = [
        ('1', '1 - High'),
        ('2', '2 - Medium'),
        ('3', '3 - Low'),
    ]

    # The number of users impacted to escalate the priority
    ESCALATE_THRESHOLD = 10

    # Ticket class attributes
    title = models.CharField(max_length=50)
    date_opened = models.DateTimeField("date opened", default=timezone.now)
    ticket_category = models.ForeignKey(TicketCategory, on_delete=models.CASCADE)
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default=3)
    users_impacted = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Open')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='assigned_tickets', null=True,
                                    blank=True)
    date_closed = models.DateTimeField("date closed", null=True, blank=True)
    resolution_tags = models.CharField(max_length=100, blank=True)

    # Actions to take on ticket submission
    def save(self, *args, **kwargs):
        # Check if the ticket was closed without a manual date entry
        if self.status == 'Closed' and not self.date_closed:
            self.close_date = timezone.now()
        # Check if the number of affected users is at or above 10
        if self.users_impacted >= self.ESCALATE_THRESHOLD:
            # Set priority to '2' (Medium)
            self.ticket_priority = '2'
        super().save(*args, **kwargs)

    # Check if the given user is allowed to modify resolution tags.
    def can_modify_resolution_tags(self, user):
        # Admins can modify resolution tags, and only after the ticket is closed.
        return user.is_staff and self.status == 'Closed'

    def __str__(self):
        # Use the ticket title as the string return for this object
        return self.title

    def was_opened_recently(self):
        # Determine if the incident was opened in the past x days
        return self.date_opened >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    # Comment class attributes
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    date_opened = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=500)
    thumbs_up = models.IntegerField(default=0)

    def __str__(self):
        # Returns the comment message when class is called as a string
        return self.message
