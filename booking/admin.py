from django.contrib import admin
from .models import TimeSlot, Table, TableSlot, Package, Booking

# Register your models here.
admin.site.register(TimeSlot)
admin.site.register(Table)
admin.site.register(TableSlot)
admin.site.register(Package)
admin.site.register(Booking)
