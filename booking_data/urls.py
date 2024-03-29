from . import views
from django.urls import path

urlpatterns = [
    path('makebooking', views.booking, name='booking'),
    path('reservations/',
         views.BookingReservationList.as_view(), name='reservations'),
    path('amend/<reservation_id>',
         views.AmendBookingReservationList, name='amend'),
    path('cancel/<reservation_id>', views.cancel_reservation, name='cancel'),
]
