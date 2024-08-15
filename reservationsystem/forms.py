from django import forms
from .models import ReservationSystem
from django.forms.widgets import DateInput, TimeInput
from django.core.exceptions import ValidationError
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = ReservationSystem
        fields = ['booking_name', 'telephone_number', 'number_of_people', 'date', 'time', 'comments']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'booking_name': 'Booking Name',
            'telephone_number': 'Telephone Number',
            'number_of_people': 'Number Of People',
            'date': 'Date',
            'time': 'Time',
            'comments': 'Additional Comments',
        }

    def clean_booking_name(self):
        booking_name = self.cleaned_data.get('booking_name')

        if not booking_name:
            raise ValidationError("Booking name is required.")
        return booking_name

    def clean_telephone_number(self):
        telephone_number = self.cleaned_data.get('telephone_number')
        if not telephone_number:
            raise ValidationError("Telephone number is required.")
        if not telephone_number.isdigit():
            raise ValidationError("Telephone number must contain only digits.")
        if len(telephone_number) < 10:
            raise ValidationError("Telephone number must be at least 10 digits long.")
        return telephone_number

    def clean_date(self):
        reservation_date = self.cleaned_data.get('date')
        if reservation_date is None:
            raise ValidationError("Date is required.")
        if reservation_date < date.today():
            raise ValidationError("The reservation date cannot be in the past.")
        return reservation_date


    def clean_comments(self):
        comments = self.cleaned_data.get('comments')
        return comments

    