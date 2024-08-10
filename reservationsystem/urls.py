from django.urls import path
from .views import AddBooking, UserBookings, EditBooking, DeleteBooking
from . import views 

app_name = 'bookings'


urlpatterns = [
    
    path('view_reservation', UserBookings.as_view(), name='view_reservation'),
    path('add_booking', AddBooking.as_view(), name='add_booking'),
    path('edit/<int:pk>', EditBooking.as_view(), name='edit_reservation'),
    path('delete/<int:pk>/', DeleteBooking.as_view(), name='delete_reservation'),
      
    
]