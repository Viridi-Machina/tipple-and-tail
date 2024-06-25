from django.contrib import admin
from .models import TippleUser, Comment, Enquiry

# Register your models here.
admin.site.register(TippleUser)
admin.site.register(Comment)
admin.site.register(Enquiry)