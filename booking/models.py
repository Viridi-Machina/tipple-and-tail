from django.db import models
from django.contrib.auth.models import User
from about.models import Event
from .constants import TIME_SLOT_OPTIONS, CAPACITY

# Models revised and refined with help from Mentor Gareth McGirr

class Table(models.Model):
    """
    Model for table creation. Uses constants for predefined timeslots and table sizes. 
    """
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField(choices=CAPACITY)

    class Meta:
        """
        Ordering for tables in ascending order.
        """
        ordering = ['number']

    def __str__(self):
        return f"Table {self.number} - {self.capacity} People" 


class Package(models.Model):
    """
    Model for package creation and reference.
    """
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.CharField(max_length=10, default="£")

    def __str__(self):
        return f"{self.title}"


class Booking(models.Model):
    """
    Model for booking creation.
    """
    booking_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_guest")
    booking_date = models.DateField(auto_now_add=True)
    booking_size = models.IntegerField(default=2)
    booking_table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="booking_table")
    booking_slot = models.IntegerField(choices=TIME_SLOT_OPTIONS, default=1)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name="booking_package", null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event", null=True)
    allergies = models.BooleanField(default=False)
    special = models.CharField(max_length=250)

    class Meta:
        """
        Ordering for date followed by booking time.
        """
        ordering = ['booking_date', 'booking_slot']

    def __str__(self):
        return (f"{self.pk} | {self.booking_date} | {self.booking_slot}")