from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Room, RoomCombination, Reservation


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone_number', 'role', 'birthdate')}),
    )
    list_display = ['username', 'email', 'role', 'is_staff']


admin.site.register(User, CustomUserAdmin)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'capacity_single')
    search_fields = ('room_name',)


@admin.register(RoomCombination)
class RoomCombinationAdmin(admin.ModelAdmin):
    list_display = ('combination_name', 'max_capacity')
    search_fields = ('combination_name',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'reserved_date', 'reserved_time',
                    'number_of_guests', 'status')
    list_filter = ('status', 'reserved_date')
    search_fields = ('user__username', 'status')
