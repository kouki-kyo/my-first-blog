from dataclasses import field
from django import forms
from .models import DailyReport

class DailyReportForm(forms.ModelForm):
    class Meta:
        model = DailyReport
        fields = '__all__'
        labels = {
            'name': '名前',
            'work_description': '業務内容',
            'wow_point': 'WOWポイント',
            'source_of_improvement': '成長の種'
        }
        help_text = {
            'name': '名前を入力',
            'work_description': '業務内容を入力',
            'wow_point': 'WOWポイントを入力',
            'source_of_improvement': '成長の種を入力'
        }