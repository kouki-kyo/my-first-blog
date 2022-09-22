from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.MainView.dashboard_view, name='main'),
]