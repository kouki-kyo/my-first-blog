from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.MainView.dashboard_view, name='main'),
    path('dailyreports', views.MainView.daily_report_list, name='daily_report_list'),
    path('dailyreports/new', views.MainView.new_daily_report, name='new_daily_report'),
]