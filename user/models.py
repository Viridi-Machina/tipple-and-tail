from django.db import models
from django.contrib.auth.models import User
from about.models import Event

ACCOUNT_STATUS = ((0, "Active"), (1, "Restricted"), (2, "Inactive"))


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
    
# User details are repeated here so that users without an active account can still make an enquiry.
# The form will be automatically filled in and hidden if the user is logged in.
class Enquiry(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(default="")
    mobile = models.CharField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Enquiry from {self.first_name}"