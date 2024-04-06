# Defines forms for submitting vulnerability reports

from django import forms
from .models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'description', 'category', 'severity', 'submitted_by']