from django.urls import path
from .views import AddBooking, UserBookings

urlpatterns = [
    path('', UserBookings.as_view(), name='view_reservation'),
    path('add', AddBooking.as_view(), name='add_booking'),
    
]