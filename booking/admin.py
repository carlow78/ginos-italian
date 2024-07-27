from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = (
        'booking_name',
        'telephone_number',
    )


