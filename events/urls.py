from django.urls import path
from . import views
from .views import HomeView, EventDetailView, AddEventView, UpdateEventView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('event/<int:pk>', EventDetailView.as_view(), name='event-details'),
    path('add_event/', AddEventView.as_view(), name='add-event'),
    path('update_event/<int:pk>', UpdateEventView.as_view(), name='update-event'),
]
