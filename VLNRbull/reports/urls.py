# INF601 - Advanced Programming in Python
# Austin Howard
# Mini Project 4

from django.urls import path, include
from . import views

urlpatterns = [
    # ex: /reports/
    path('', views.index, name='index'),
    # ex: /reports/vulnerabilities
    path('vulnerabilities/', views.VulnerabilityListView.as_view(), name='vulnerabilities'),
    # ex: /reports/vulnerabilities/1
    path('vulnerabilities/<int:pk>', views.VulnerabilityDetailView.as_view(), name='vulnerability-detail-view'),
    # ex: /reports/systems
    path('systems/', views.SystemsListView.as_view(), name='systems'),
    # ex: /reports/systems/1
    path('systems/<int:pk>/', views.SystemDetailView.as_view(), name='system-detail-view'),

]