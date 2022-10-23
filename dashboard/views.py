from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from . import matplotlib
import random

from .forms import DailyReportForm
from .models import DailyReport

class MainView(TemplateView, LoginRequiredMixin):
    def dashboard_view(request):
        template_name = 'dashboard/main.html'

        chart_labels = [chr(ord("A")+i) for i in range(7)]
        list_chart_data_x = [[random.randint(-100, 100) for _ in range(7)] for _ in range(2)]
        list_chart_data_xyr = [[{'x': random.randint(-100, 100), 'y': random.randint(-100, 100), 'r': random.randint(1, 10)} for _ in range(7)] for _ in range(2)]

        chart_matplotlib = matplotlib.plot_graph(chart_labels, list_chart_data_x[0])

        context = {
            'chart_labels': chart_labels,
            'list_chart_data_x': list_chart_data_x,
            'list_chart_data_xyr': list_chart_data_xyr,
            'len_data': len(chart_labels),
            'chart_matplotlib': chart_matplotlib
        }
        return render(request, template_name, context)
    
    def new_daily_report(request):
        user_name = request.user
        template_name = 'daily_report/daily_report_form.html'
        if request.method == "POST":
            form = DailyReportForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('dashboard:daily_report_list'))
            else:
                context = {
                    'form': form
                }
                return render(request, template_name, context)
        else:
            form = DailyReportForm()
        return render(request, template_name, {'form': form, 'user_name': user_name})
    
    def daily_report_list(request):
        template_name = 'daily_report/daily_report_list.html'
        daily_reports = DailyReport.objects.order_by('-created')
        return render(request, template_name, {'daily_reports': daily_reports})