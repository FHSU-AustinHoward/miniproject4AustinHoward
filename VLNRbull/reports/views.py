# Implement views for handling report submissions and reviews

from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report


def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_submitted')
    else:
        form = ReportForm()
    return render(request, 'reports/submit_report.html', {'form': form})


def report_submitted(request):
    return render(request, 'reports/report_submitted.html')


def review_reports(request):
    reports = Report.objects.filter(is_reviewed=False)
    return render(request, 'reports/review_reports.html', {'reports': reports})


def mark_as_reviewed(request, report_id):
    report = Report.objects.get(id=report_id)
    report.is_reviewed = True
    report.save()
    return redirect('review_reports')
