from django.db import models
from django.contrib.auth.models import User
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