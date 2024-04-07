from django.urls import path
from . import views

# Define the application namespace
app_name = "tickets"

# URL patterns for the ticket application
urlpatterns = [
    # ex: /tickets/
    path("", views.IndexView.as_view(), name="index"),

    # ex: /tickets/1/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # ex: /tickets/1/privileged/
    path("<int:pk>/privileged/", views.PrivilegedView.as_view(), name="privileged"),
]