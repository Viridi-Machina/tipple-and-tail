from . import views
from django.urls import path


urlpatterns = [
    path('', views.about, name='home'),
    path('events/', views.EventList.as_view(), name='events')
]