from django import forms
from .models import Booking_data
from .widget import DatePickerInput, TimePickerInput
from . import validators


class Booking_dataForm(forms.ModelForm):
    """
    this is a test for booking form
    """
   
    mobile = forms.CharField(
        label='Contact Number',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Mobile'}),
    )

    date = forms.DateField(
        label='Date of Booking',
        required=True,
        widget=DatePickerInput(),
       
    )

    time = forms.TimeField(
        label='Arrival Time',
        required=True,
        widget=TimePickerInput(),
       
    )

    notes = forms.CharField(
        label='Special Requirements',
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Please enter additional requirements here.'
        }),
        max_length=300,
    )

    attendees = forms.IntegerField(
        label='Number of Attendees',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Attendess'}),
    )

    class Meta:
        """
        The booking form inherits from the Booking model.
        Takes the required fields needed for a user to make a new booking.
        Defines the widgets for the date and time fields.
        """
        model = Booking_data

        fields = (
            'mobile', 'date', 'time', 'notes', 'attendees'
        )

        widgets = {
            'date': DatePickerInput,
            'time': TimePickerInput,
        }

       