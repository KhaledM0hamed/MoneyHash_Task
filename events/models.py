from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date 
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)

    def __repr__(self):
        return {
            'title': self.title,
            'author': str(self.author),
            'description': self.description,
            'date': self.date
        }

    def get_absolute_url(self):
        return reverse("event-details", args=[self.id])
    
    @property
    def is_past_due(self):
        return date.today() > self.date    
