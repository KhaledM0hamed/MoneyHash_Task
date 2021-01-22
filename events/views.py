from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Event
from .forms import EventForm, EventEditForm
# # Create your views here.
# def home(request):
#     context = {}
#     return render(request, 'home.html', context)

class HomeView(ListView):
    model = Event
    template_name = 'home.html'
    ordering = ['-date']
    paginate_by = 5

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_details.html'

class AddEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'add_event.html'

class UpdateEventView(UpdateView):
    model = Event
    template_name = 'update_event.html'
    form_class = EventEditForm
