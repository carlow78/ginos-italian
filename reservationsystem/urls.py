from django.urls import path
from django.views.static import serve
from django.conf import settings
from .views import AddBooking, UserBookings, EditBooking, DeleteBooking, Menu
from . import views 

"""
Template folder name
"""
app_name = 'bookings' 


"""
The below are the urls for the reservationsystem app
"""

urlpatterns = [
    
    path('view_reservation', UserBookings.as_view(), name='view_reservation'),
    path('menu', views.Menu.as_view(), name='menu'),
    path('add_booking', AddBooking.as_view(), name='add_booking'),
    path('edit/<int:pk>', EditBooking.as_view(), name='edit_reservation'),
    path('delete/<int:pk>/', DeleteBooking.as_view(), name='delete_reservation'),
      
    
]