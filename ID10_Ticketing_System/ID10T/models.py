from django.db import models


# Create your models here.
class ServiceCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.PROTECT)
    date_time = models.DateTimeField()
    urgency = models.CharField(max_length=10, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
     ])
    users_impacted = models.PositiveIntegerField()

    def __str__(self):
        return self.title

