""" This module contains custom functions used for form validation. """

import datetime
from django.core.exceptions import ValidationError


def validate_opening_hour(value):
    """
    A custom validation function.
    Intended for use on the time field of the BookingForm.
    Ensures the input value is between 11AM and 9PM.
    If validation is failed the custom error message is returned.
    """
    if not 11 <= int(value.hour) <= 21:
        raise ValidationError(
            'We only take reservations between 11AM & 9PM',
            params={'value': value},
        )


def validate_future_date(value):
    """
    A custom validation function.
    Intended for use on date field of the BookingForm.
    Using the datetime method datetime.date.today
    ensures the input value is a future date.
    If validation is failed the custom error message is returned.
    If value is equal to current day provides an alternate error message.
    """
    if value < datetime.date.today():
        raise ValidationError(
            'Please select a future date',
            params={'value': value},
        )

    elif value == datetime.date.today():
        raise ValidationError(
            'Please call to make same day reservations',
            params={'value': value},
        )


def validate_open_day(value):
    """
    A custom validation function.
    Intended for use on the date field of the BookingForm.
    Uses the Weekday method of the datetime library.
    Ensures the input value is not a Monday or a Sunday.
    If validation is failed the custom error message is returned.
    """
    if value.weekday() == 0:
        raise ValidationError(
            'We are closed on a Monday, please choose a differant date',
            params={'value': value},
        )
    elif value.weekday() == 6:
        raise ValidationError(
            'We are closed on a Sunday, please choose a differant date',
            params={'value': value},
        )


def validate_attendees_size(value):
    """
    A custom validation function.
    intended for use on the 'guests' field of the Booking_dataForm.
    If input integer is less than 10,
    validation is failed and the custom error message is returned.
    If value is equal to zero, a validation message pops-up alerting the user.
    """
    if value < 10:
        raise ValidationError(
            'We do not accept booking reservation of less than 10 attendees.\n'
            'Attendees must be at least 10 attending for a booking to be accepted.',
            params={'value': value},
        )