from django.test import TestCase, Client
from django.urls import reverse
from reservationsystem.models import ReservationSystem
from  .views import EditBooking, DeleteBooking
from django.contrib.auth.models import User

class TestBooking(TestCase):
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
            'booking_id': 1,
            'booking_name': 'Tom',
            'telephone_number': '03456754',
            'number_of_people': 4,
            'date': '2024-08-15', 
            'time': '19:00',
            'comments': 'None',
        })
        
        # Check that the reservation was created successfully
        self.assertEqual(response.status_code, 302)  
        

    def setUp(self):

        self.kwargs = {'pk': 1}

    def test_edit_reservation(self):
        # Test edit a reservation. Changing no of people from 4 to 6

            self.client.login(username='Tom', password='MagnumPI')
            booking_id = self.kwargs.get('pk')
            response = self.client.post(reverse('bookings:edit_reservation', kwargs={'pk': booking_id}))
            {
            'booking_name': 'Tom',
            'telephone_number': '03456754',
            'number_of_people': 6,
            'date': '2024-08-15', 
            'time': '19:00',
            'comments': 'None',
        }
            # Check that the reservation was successfully edited
            self.assertEqual(response.status_code, 302)

    def test_delete_reservation(self):
            # Test to delete a reservation
            self.client.login(username='Tom', password='MagnumPI')
            booking_id = self.kwargs.get('pk')
            response = self.client.post(reverse('bookings:delete_reservation', kwargs={'pk': booking_id}), follow=True)

            # Check that the reservation was successfully deleted    
            self.assertEqual(response.status_code, 200)  

class TestView(TestCase):


    def test_home_view_get(self):
       
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html', 'base.html')

    def test_menu_view_get(self):
       
        response = self.client.get(reverse('bookings:menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/menu.html', 'base.html')

    def test_addbooking_view_get(self):

        self.client.login(username='Tom', password='MagnumPI')
        response = self.client.get(reverse('bookings:add_booking'))
        self.assertEqual(response.status_code, 302)
    


