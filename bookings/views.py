from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import User, Reservation


@login_required
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


@login_required
def reservation_success(request):
    return render(request, 'bookings/reservation_success.html')


def register(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            phone_number=phone_number
        )

        login(request, user)
        return redirect('create_reservation')

    return render(request, 'bookings/register.html')
