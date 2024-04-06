from django.urls import path
from . import views
from .views import user_login

urlpatterns = [
    # Add  URL patterns as needed
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('login/', user_login, name='login'),
    path('register/', views.user_register, name='register'),
]