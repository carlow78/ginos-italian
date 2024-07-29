from django.contrib import admin
from .models import reservationsystem

@admin.register(reservationsystem)
class ReservationSystemAdmin(admin.ModelAdmin):
    model = reservationsystem
    list_display = (
        'date',
        'booking_name',
        'telephone_number',
    )


