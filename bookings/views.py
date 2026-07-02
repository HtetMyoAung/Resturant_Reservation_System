from django.shortcuts import render, redirect
# ၁။ ဒီလိုင်းကို ပေါင်းထည့်ပါ
from django.contrib.auth.decorators import login_required
from .models import Reservation


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
