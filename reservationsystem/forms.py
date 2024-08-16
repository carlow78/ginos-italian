from django import forms
from .models import ReservationSystem
from django.forms.widgets import DateInput, TimeInput
from django.core.exceptions import ValidationError
from datetime import date
from django.forms import Textarea


class BookingForm(forms.ModelForm):

    """
    The restaurant's reservation form. All fields are required except for comments.
    Telephone number has to be at least 10 (and max 15) digits only.
    Past dates are not excepted.
    Drop-down boxes for No. of people and Booking Time.
    User will be prompted with red error messages for invalid input ie: past date.
    Validation thanks to - https://stackoverflow.com/questions/12278753/clean-method-in-model-and-field-validation

    """
    class Meta:
        model = ReservationSystem
        fields = ['booking_name', 'telephone_number', 'number_of_people', 'date', 'time', 'comments']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'comments': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }

        labels = {
            'booking_name': 'Booking Name',
            'telephone_number': 'Telephone Number',
            'number_of_people': 'Number Of People',
            'date': 'Date',
            'time': 'Time',
            'comments': 'Additional Comments',
        }
        help_texts = {
            'telephone_number': 'Please enter your phone number including area code (if applicable).',
            'comments': 'Any special requests/notes ? (this field can be left blank).',
        }

    def clean_booking_name(self):
        booking_name = self.cleaned_data.get('booking_name')
        if not booking_name:
            raise ValidationError("Booking name is required.")
        if booking_name.isdigit():
            raise ValidationError("Booking name cannot be an integer.")
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


    