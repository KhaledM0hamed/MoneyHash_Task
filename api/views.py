from django.http import JsonResponse
from events.models import Event
from django.core import serializers
from django.contrib.auth.decorators import login_required

@login_required()
def addParticipant(request, event_pk, participant_pk):
    if request.method == 'POST':
        event = Event.objects.filter(id=event_pk)
        try:
            event[0].participants.add(participant_pk)
            responseData = {
                'msg': 'success'
            }
        except:
            responseData = {
                'msg': 'failed'
            }

        return JsonResponse(responseData)
    elif request.method == 'DELETE':
        event = Event.objects.filter(id=event_pk)
        try:
            event[0].participants.remove(participant_pk)
            responseData = {
                'msg': 'success'
            }
        except:
            responseData = {
                'msg': 'failed'
            }

        return JsonResponse(responseData)
    else:
            responseData = {
                'msg': "you don't have permission to do that idiot!"
            }
            return JsonResponse(responseData)