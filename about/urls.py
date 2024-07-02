from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='home'),
    path('events/', views.event_list, name='events')
]
