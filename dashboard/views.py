from django.shortcuts import render
from django.views.generic import TemplateView
from . import matplotlib

import random

class MainView(TemplateView):
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