from django.shortcuts import render
from .models import Event, About


def about(request):
    """
    Renders the about section on the home dashboard.
    """
    about = About.objects.all().first()

    return render(request, "about/index.html", {"about": about},)


def event_list(request):
    """
    Renders the events list page.
    """
    events = Event.objects.all().order_by("-event_date")
    context = {
        "events": events,
    }

    return render(request, "about/event_list.html", context,)

