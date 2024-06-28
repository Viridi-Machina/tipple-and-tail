from django.db import models
from django.contrib.auth.models import User
from about.models import Event
from .constants import STATUS, TAKEN, TIME_SLOT_OPTIONS


class TimeSlot(models.Model):
    time_in = models.CharField(max_length=8, choices=TIME_SLOT_OPTIONS, default="18:00")
    time_out = models.CharField(max_length=8, choices=TIME_SLOT_OPTIONS, default="18:00")

    def __str__(self):
        return f"{self.time_in} - {self.time_out}"


class Table(models.Model):
    number = models.SmallIntegerField()
    capacity = models.SmallIntegerField()

    def __str__(self):
        return f"Table {self.number} - {self.capacity} People" 


class TableSlot(models.Model):
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="tables")
    time_slot_id = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name="time_slot")
    status = models.IntegerField(choices=TAKEN, default=0)

    def __str__(self):
        return f"T{self.table_id.number} | {self.time_slot_id}"


class Package(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=10, default="£")

    def __str__(self):
        return f"{self.title}"


class Booking(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")
    date = models.DateField(auto_now_add=True)
    guests = models.SmallIntegerField(default=2)
    table_id = models.ManyToManyField(TableSlot)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name="booking_slot")
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name="package")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event")
    allergies = models.BooleanField(default=False)
    special = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return (f"{self.user_id} | {self.date} | {self.guests} | "
                f"{self.table_id} | {self.time_slot} | {self.package} | "
                f"{self.allergies}")