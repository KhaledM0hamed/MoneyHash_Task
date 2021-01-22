from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'author', 'description', 'date')

        widgets= {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea   (attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EventEditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date')

        widgets= {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea   (attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
        }