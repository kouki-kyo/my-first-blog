from django.db import models
from django.utils.timezone import localtime

class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class DailyReport(Timestamp):
    name = models.CharField(max_length=100)
    work_description = models.CharField(max_length=100)
    wow_point = models.CharField(max_length=100)
    source_of_improvement = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ':' + self.created.strftime('%Y/%m/%d %H:%M')
