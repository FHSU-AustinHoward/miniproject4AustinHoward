from django.urls import path

from . import views


# Configures ticket.py application's URLs into a logical pattern
urlpatterns = [
    # ex: /tickets/
    path("", views.index, name="index"),
    # ex: /tickets/1
    path("<int:ticket_id>/", views.detail, name="detail")
]