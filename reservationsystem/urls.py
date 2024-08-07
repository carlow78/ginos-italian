from django.urls import path
from .views import AddBooking, UserBookings, EditBooking
from . import views 

app_name = 'bookings'
#reversed('app_name:updated_booking')

urlpatterns = [
     path('view_reservation', UserBookings.as_view(), name='view_reservation'),
    path('add_booking', AddBooking.as_view(), name='add_booking'),
    path('edit/<int:pk>', EditBooking.as_view(), name='edit_reservation'),
    #path('bookings/update/<int:id>/', UpdateBooking.as_view(), name='updated_booking'),
    
]