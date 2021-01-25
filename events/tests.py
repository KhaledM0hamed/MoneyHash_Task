from django.test import TestCase, Client
from .models import Event
from members.models import CustomUser
# Create your tests here.

class EventTestCase(TestCase):

    def setUp(self):
        # Create Participant
        u1 = CustomUser.objects.create(username='test1', password='qweasd123123', email='test@test.com')
        u2 = CustomUser.objects.create(username='test2', password='qweasd123123', email='test2@test.com')
        u3 = CustomUser.objects.create(username='test3', password='qweasd123123', email='test3@test.com')
        
        # Create Events
        e1 = Event.objects.create(title='test1', author=u1, description='test', date='2022-01-26')
        e2 = Event.objects.create(title='test2', author=u2, description='test', date='2022-01-26')
        e3 = Event.objects.create(title='test3', author=u3, description='test', date='2022-01-26')

    def test_add_participate(self):
        event = Event.objects.get(title="test1")
        user = CustomUser.objects.get(username="test1")
        
        # Add participants to Events 
        event.participants.add(user)
        event.save()

        self.assertEqual(event.participants.count(), 1)

    def test_valid_events_page(self):
        c = Client()
        response = c.get(f"/?page=1")
        self.assertEqual(response.status_code, 200)

    def test_invalid_events_page(self):

        c = Client()
        response = c.get(f"/?page=3")
        self.assertEqual(response.status_code, 404)