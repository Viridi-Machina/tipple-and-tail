from django.db import models
from user.models import TippleUser


# class Booking(models.Model):
#     user_id = models.ForeignKey(
#         TippleUser, on_delete=models.CASCADE, 
#         related_name="bookings"
#     )
#     guests = models.SmallIntegerField()
#     table_id = models.ForeignKey(
#         TableSlot, on_delete=models.CASCADE, 
#         related_name="tables"
#     )
#     allergies = models.BooleanField(default=False)
#     time_slot_id = models.ForeignKey(
#         TimeSlot, on_delete=models.CASCADE, 
#         related_name="time_slot"
#     )
#     created_by = models.ForeignKey(

#     )