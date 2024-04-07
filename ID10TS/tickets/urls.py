from django.urls import path

from . import views


# Configures ticket.py application's URLs into a logical pattern
app_name = "tickets"
urlpatterns = [
    # ex: /tickets/
    path("", views.index, name="index"),
    # ex: /tickets/home
    path("home", views.home, name="home"),
    # ex: /tickets/1
    path("<int:ticket_id>/", views.detail, name="detail"),
    # ex: /tickets/1/privileged
    path("<int:ticket_id>/privileged/", views.privileged, name="privileged"),
]
