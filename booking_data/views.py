import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from booking_data.models import Booking_data
from django.contrib import messages
from django.db import IntegrityError
from .models import Booking_data
from .forms import Booking_dataForm


def booking(request):
    """
    Uses an if/else statement to assert the user attempting
    to access the booking feature is an authenticated user,
    if not redirects to the sign in page. Otherwise
    renders the Booking_dataForm on the booking.html template.
    On a POST request, gets the data from the Booking_dataForm,
    places the data in an instance. Checks that the instance is valid.
    If the booking is invalid the Booking_dataForm will not post,
    The fields remain populated with the POST data.
    Field validation is handled in the Booking_data model and Booking_dataForm.
    If valid saves the form without commiting,
    The valid booking then has the authorized users ID applied to it.
    The email address registered to their account as the email field.
    A try/except statement is then used to ensure the booking
    meets the Booking models unique_booking constraint.
    If it passes the booking is saved to the database.
    The user is then redirected to the reservations page.
    If it fails the error message is returned as context
    along with the POST data and displayed to the user.
    The logic for these actions is employed via an if/else loop.
    """
    if request.user.is_authenticated:

        if request.method == 'POST':
            booking_form = Booking_dataForm(request.POST)

            if booking_form.is_valid():
                user = request.user  # For use in logic below.
                current_booking = booking_form.save(commit=False)
                messages.success(request, 'Booking Successful')
                current_booking.user = user
                current_booking.email = user.email

                try:
                    current_booking.save()
                except IntegrityError as error:
                    error = (
                        'You have already requested this reservation'
                    )
                    return render(request, 'booking.html', {
                        "booking_form": Booking_dataForm(request.POST),
                        'error': error,
                    })

                return redirect(reverse("reservations"))

            else:
                return render(request, 'booking.html', {
                    "booking_form": Booking_dataForm(request.POST)
                })

        else:
            return render(request, 'booking.html', {
                "booking_form": Booking_dataForm()
            })

    else:
        return redirect(reverse("account_login"))


class BookingReservationList(generic.ListView):
    """
    Each individual booking within the Booking model,
    is now referred to as a reservation for clarity.
    Class based view that inherits from the Booking model.
    """
    model = Booking_data

    def sort(self, bookings):
        """
        A helper method for the BookingReservationsList class.
        Takes the bookings variable created in the get method.
        Each individual booking from this vairable is iterated over,
        all instances are checked to ensure the date field is a
        future date, done with the datetime.date.today method
        from the datetime package. Instances that have passed are marked false.
        The remaining reservations are marked true
        and returned back to the get method.
        """
        if bookings.date >= datetime.date.today():
            return True
        else:
            return False

    def get(self, request, *args, **kwargs):
        """
        Uses an if/else statement to assert user authentication,
        if failed redirects to the login page.
        If passes uses the inbuilt get method to filter reservations,
        by ones with the authorized users ID. Then calls the sort method.
        Only upcoming reservations are displayed.
        Renders to the 'reservations.html' template.
        """
        if request.user.is_authenticated:
            bookings = Booking_data.objects.filter(user=request.user)
            reservations = filter(self.sort, bookings)

            return render(
                request, 'reservations.html',
                {
                    'reservations': reservations,
                },
            )

        else:
            return redirect(reverse("account_login"))


def AmendBookingReservationList(request,reservation_id):  
    if request.user.is_authenticated:
        reservation = get_object_or_404(Booking_data, id=reservation_id)
        current_user = request.user

        if request.method == 'POST':
            booking_form = Booking_dataForm(request.POST, instance=reservation)
            if booking_form.is_valid():
                booking_form.save()
                messages.success(request, 'Booking updated successfully.')
                return redirect(reverse("reservations"))
        else:
            booking_form =Booking_dataForm(instance=reservation) 
        return render(request, 'amend_booking.html', {'booking_form': Booking_dataForm, 'reservation':reservation})  
    else:
        return redirect(reverse("account_login"))             
       

def cancel_reservation(request, reservation_id):
    """
    Uses an if/else statement to assert the user attempting
    to access the cancel feature is an authenticated user,
    if not redirects to the sign in page.
    If the signed in user is authenticated
    a copy of the reservation from the Booking database is created.
    The signed in users ID is then compared to the reservations user ID.
    If not equal they are redirected to the sign in page.
    If equal the reservation is deleted from the database via its unique id,
    the user is then redirected back to the reservations.html page.
    """
    if request.user.is_authenticated:
        reservation = get_object_or_404(Booking_data, id=reservation_id)
        current_user = request.user

        if current_user == reservation.user:
            reservation.delete()
            return redirect(reverse("reservations"))

        else:
            return redirect(reverse("reservations"))

    else:
        return redirect(reverse("account_login"))             
           