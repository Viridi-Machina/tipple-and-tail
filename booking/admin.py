from django.contrib import admin
from .models import Table, Package, Booking

# Registry code adapted from Mentor Gareth McGirr


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """ Admin panel view of tables capacity filter. """
    list_display = (
        'number',
        'capacity',
    )
    list_filter = ('capacity',)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    """ Admin panel view of created packages. """
    list_display = (
        'title',
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Admin panel view of bookings using date range filter package. """
    list_display = (
        'pk',
        'booking_date',
        'booking_slot',
        'booking_name',
        'booking_table',
        'booking_size',
        'event',
        'allergies',
    )
    list_filter = (
        'booking_slot', 'booking_table',
    )
