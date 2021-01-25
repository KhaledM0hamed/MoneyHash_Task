from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Event
from .forms import EventForm, EventEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime


class HomeView(ListView):
    model = Event
    template_name = 'home.html'
    ordering = ['-date']
    paginate_by = 4

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_details.html'

class AddEventView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'add_event.html'
    login_url = '/members/login'

    

class UpdateEventView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = 'update_event.html'
    form_class = EventEditForm
    login_url = '/members/login'


