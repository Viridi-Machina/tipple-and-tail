from . import views
from django.urls import path


urlpatterns = [
    path('', views.about, name='home'),
    path('events/', views.event_list, name='events')
]