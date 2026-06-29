from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, default='customer')
    birthdate = models.DateField(blank=True, null=True)


class Room(models.Model):
    room_name = models.CharField(max_length=100, unique=True)
    capacity_single = models.PositiveIntegerField(default=4)


class RoomCombination(models.Model):
    combination_name = models.CharField(max_length=150, unique=True)
    max_capacity = models.PositiveIntegerField()
    rooms = models.ManyToManyField(Room)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reserved_date = models.DateField()
    reserved_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    number_of_guests = models.PositiveIntegerField()
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    blocked_rooms = models.ManyToManyField(Room)
