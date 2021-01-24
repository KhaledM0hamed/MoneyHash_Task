from django.urls import path
from . import views

urlpatterns = [
    path('event/<int:event_pk>/participant/<int:participant_pk>', views.addParticipant, name='add-participant')
]
