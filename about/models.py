from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "New"), (1, "Expired"))

class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"About Content"
    

class Event(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    event_date = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | {self.event_date}"