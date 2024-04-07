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
        # Modify as needed
    ]

    # Ticket class attributes
    ticket_title = models.CharField(max_length=50)
    open_date = models.DateTimeField("date opened")
    ticket_category = models.ForeignKey(TicketCategory, on_delete=models.CASCADE)
    ticket_priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default='3')
    users_impacted = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    ticket_description = models.CharField(max_length=500)
    ticket_status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Open')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='assigned_tickets', null=True,
                                    blank=True)
    close_date = models.DateTimeField("date closed", null=True, blank=True)
    resolution_tags = models.CharField(max_length=100, blank=True)

    # Actions to take on ticket submission
    def save(self, *args, **kwargs):
        # Check if the ticket was closed without a manual date entry
        if self.ticket_status == 'Closed' and not self.close_date:
            self.close_date = timezone.now()
        # Check if the number of affected users is at or above 10
        if self.users_impacted >= 10:
            # Set priority to '2' (Medium)
            self.ticket_priority = '2'
        super().save(*args, **kwargs)

    # Check if the given user is allowed to modify resolution tags.
    def can_modify_resolution_tags(self, user):
        # Admins can modify resolution tags, and only after the ticket is closed.
        return user.is_staff and self.ticket_status == 'Closed'

    def __str__(self):
        # Use the ticket title as the string return for this object
        return self.ticket_title

    def was_opened_recently(self):
        # Determine if the incident was opened in the past ..........˅˅˅˅˅˅
        return self.open_date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    # Comment class attributes
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment_text = models.CharField(max_length=500)
    thumbs_up = models.IntegerField(default=0)

    def __str__(self):
        # Returns the comment content when class is called as a string
        return self.comment_text
