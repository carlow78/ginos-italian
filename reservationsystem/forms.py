from django import forms

from .models import ReservationSystem
from django.forms import DateInput, TimeInput
from datetime import date

class DateInput(forms.DateInput):

    input_type = 'date'

class BookingForm(forms.ModelForm):

    class Meta:
        model = ReservationSystem
        widgets = {
            'date': DateInput(),
        }
        fields = ['booking_name', 'telephone_number', 'number_of_people', 'date', 'time', 'comments']

    labels = {

        'booking_name':'Booking Name',
        'telephone_number': 'Telephone Number',
        'number_of_people': 'Number Of People',
        'date': 'Date',
        'time': 'Time',
        'comments': 'Additional Comments',
    }


    