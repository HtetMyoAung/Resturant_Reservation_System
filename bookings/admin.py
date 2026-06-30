from django.contrib import admin
from .models import User, Room, RoomCombination, Reservation


admin.site.register(User)
admin.site.register(Room)
admin.site.register(RoomCombination)
admin.site.register(Reservation)
