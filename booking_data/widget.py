""" This module contains widgets used on the booking form. """

from django import forms


class DatePickerInput(forms.DateInput):
    """
    Defines the date picker widget used in the Booking_dataForm.
    The Booking_dataForm is found in forms.py in the booking_data directory.
    """
    input_type = 'date'


class TimePickerInput(forms.TimeInput):
    """
    Defines the time picker widget used in the Booking_dataForm.
    The BookingForm is found in forms.py in the booking_data directory.
    """
    input_type = 'time'
