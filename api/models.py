from calendar import Calendar
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class CalenderEvent(models.Model):
    email = models.EmailField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Calender Event'
        verbose_name_plural = 'Calender Events'

    