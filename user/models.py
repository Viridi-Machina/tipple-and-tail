from django.db import models
from about.models import Event 

STATUS = ((0, "Active"), (1, "Restricted"), (2, "Inactive"))

# A new user model has been created rather than using the default user model.
# This is so that extra user information can be provided to the database,
# including the account status and bookings made by the user.
class TippleUser(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField
    mobile = models.IntegerField()
    # bookings foreign key
    status = models.IntegerField(choices=STATUS, default=0)


class Comment(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, 
        related_name="comments"
    )
    author = models.ForeignKey(
        TippleUser, on_delete=models.CASCADE, 
        related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
    
# Tipple user details are repeated here so that users without an active account can still make an enquiry.
# The form will be automatically filled in and hidden if the user is logged in.
class Enquiry(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField
    mobile = models.IntegerField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Enquiry from {self.name}"