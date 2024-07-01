from django.urls import path
from . import views

urlpatterns = [
    path('createbooking/', views.CreateBooking.as_view(), name='createbooking'),
    path('managebookings/', views.BookingsList.as_view(), name='managebookings'),
    path('editbooking/<slug:pk>/', views.EditBookingView.as_view(), name='editbooking'),
    path('delete/<slug:pk>/',views.DeleteBookingView.as_view(), name="delete_booking")
]