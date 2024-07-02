from django.db import models
from cloudinary.models import CloudinaryField

STATUS = ((0, "New"), (1, "Expired"))


class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"About Content"


class Event(models.Model):
    title = models.CharField(max_length=150, unique=False)
    slug = models.SlugField(max_length=150, unique=False)
    event_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | {self.event_date}"
