from django.urls import path

from . import views


# Configures ticket.py application's URLs into a logical pattern
urlpatterns = [
    path("", views.index, name="index"),
]