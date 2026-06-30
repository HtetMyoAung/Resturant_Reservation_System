from django.shortcuts import render, redirect
from .models import Reservation

# Create your views here.


def create_reservation(request):
    if request.method == 'POST':
        user = request.user
        reserved_date = request.POST.get('reserved_date')
        reserved_time = request.POST.get('reserved_time')
        number_of_guests = request.POST.get('number_of_guests')

        Reservation.objects.create(
            user=user,
            reserved_date=reserved_date,
            reserved_time=reserved_time,
            number_of_guests=number_of_guests,
            status='pending'
        )

        return redirect('reservation_success')

    return render(request, 'bookings/create_reservation.html')
