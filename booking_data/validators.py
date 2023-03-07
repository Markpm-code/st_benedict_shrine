""" This module contains custom functions used for form validation. """

import datetime
from django.core.exceptions import ValidationError


def validate_arrival_time(value):
    """
    A custom validation function.
    Intended for use on the time field of the Booking_dataForm.
    Ensures the input value is between 8AM and 1 PM.
    If validation is failed the custom error message is returned.
    """
    if not 8 <= int(value.hour) <= 13:
        raise ValidationError(
            'We only accepts arrivals beteween 8 AM to 1 PM.',
            params={'value': value},
        )


def validate_future_date(value):
    """
    A custom validation function.
    Intended for use on date field of the Booking_dataForm.
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
            'Booking must be not the current date.',
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