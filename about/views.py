from django.shortcuts import render
from django.views import generic
from .models import Event


class EventList(generic.ListView):
    queryset = Event.objects.all().order_by("-event_date")
    template_name = "about/event_list.html"

def about(request):
    return render(request, "about/index.html")

