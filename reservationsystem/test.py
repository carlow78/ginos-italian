from django.test import TestCase, Client
from django.urls import reverse
from reservationsystem.models import ReservationSystem  
from django.contrib.auth.models import User

class TestAddBooking(TestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(
            email='tom.selleck@tester.com',
            username='Tom',
            password='MagnumPI'
        )
        self.client = Client()
        self.client.login(username='Tom', password='MagnumPI')

    def test_create_reservation(self):
        # Test creating a reservation
        response = self.client.post(reverse('bookings:add_booking'), {
            'booking_name': 'Tom',
            'telephone_number': '03456754',
            'number_of_people': 4,
            'date': '2024-08-15', 
            'time': '19:00',
            'comments': 'None',
        })
        
        # Check that the reservation was created successfully
        self.assertEqual(response.status_code, 200)  
        self.assertTrue(ReservationSystem.objects.filter(booking_name='Tom').exists())
