from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, Event


# Model Registry (class)
@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
