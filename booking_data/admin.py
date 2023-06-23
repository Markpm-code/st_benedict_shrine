""" This module contains the admin logic for the booking app. """

from django.contrib import admin
from .models import Booking_data


@admin.register(Booking_data)
class Booking_dataAdmin(admin.ModelAdmin):
    """
    Allows admins a quick overview of all bookings,
    with the ability to filter by date and time for a precise overview.
    Intended for making business decisions.
    Also allows for search by booking lead.
    Containts methods to accept or decline the bookings within the dropdown.
    """
    list_display = (
        'lead', 'date', 'time', 'attendees', 'status',
        'notes', 'mobile', 'email',
        )
    list_filter = ('date', 'time',)
    search_fields = ('lead',)
    actions = ['accept_booking', 'decline_booking']

    def accept_booking(self, _request, queryset):
        """
        Allows bookings to be accepted from the dropdown menu in admin.
        2 is defined as declined in the STATUS tuple found in models.py on the
        booking directory.
        """
        for reservation in queryset:
            reservation.status = 1
            reservation.save()

    def decline_booking(self, _request, queryset):
        """
        Allows bookings to be declined from the dropdown menu in admin.
        2 is defined as declined in the STATUS tuple found in models.py on the
        booking directory.
        """
        for reservation in queryset:
            reservation.status = 2
            reservation.save()
