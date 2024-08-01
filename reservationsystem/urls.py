from django.urls import path
from .views import AddBooking, Reservation

urlpatterns = [
    path('', Reservation.as_view(), name='view_reservation'),
    path('add', AddBooking.as_view(), name='add_booking'),
    
]