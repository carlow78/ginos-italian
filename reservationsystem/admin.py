from django.contrib import admin
from .models import ReservationSystem

@admin.register(ReservationSystem)
class ReservationSystemAdmin(admin.ModelAdmin):
    model = ReservationSystem
    list_display = (
        'date',
        'time',
        'number_of_people',
        'booking_name',
        'telephone_number',
       
    )


