from . import views
from django.urls import path

urlpatterns = [
    path('makebooking', views.booking, name='booking'),
    path('', views.Booking_dataList.as_view(), name='booking.html'),
    #path('', views.Booking_dataList.as_view(), name='manage_booking.html')
    path('manage_booking', views.manage_booking, name='manage_booking.html')

]