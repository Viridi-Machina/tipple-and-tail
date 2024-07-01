from datetime import timedelta, date
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
from django.contrib import messages
from .models import Booking, Table, Package
from .forms import BookingForm


class CreateBooking(LoginRequiredMixin, CreateView):
    """
    View to render main booking page:
    Users can create a booking here.
    """
    form_class = BookingForm
    template_name = 'booking/booking.html'
    success_url = "/booking/managebookings/"
    model = Booking

    def form_valid(self, form):
        """
        Before form submission, assign table with lowest capacity
        needed for booking guests
        """
        form.instance.booking_name = self.request.user
        date = form.cleaned_data['booking_date']
        time = form.cleaned_data['booking_slot']
        guests = form.cleaned_data['booking_size']
        
        # Filter tables with capacity greater than or equal
        # to the number of guests (using __gte method)
        available_table = list(Table.objects.filter(
            capacity__gte=guests
        ))
        
        # Filter tables with the requested date
        bookings_on_requested_date = Booking.objects.filter(
            booking_date=date, booking_slot=time)
        
        # Iterate over bookings to get tables not booked
        for booking in bookings_on_requested_date:
            for table in available_table:
                if table.number == booking.booking_table.number:
                    available_table.remove(table)
                    break

        # Iterate over tables not booked to get lowest
        # capacity table to assign to booking
        lowest_capacity_table = available_table[0]
        for table in available_table:
            if table.capacity < lowest_capacity_table.capacity:
                lowest_capacity_table = table
        form.instance.booking_table = lowest_capacity_table

        messages.success(
            self.request,
            f'Booking confirmed for {guests} guests on {date}'
        )

        return super(CreateBooking, self).form_valid(form)


class BookingsList(LoginRequiredMixin, ListView):
    """
    View to render ManageBookings
    """
    model = Booking
    template_name = 'booking/managebookings.html'

    def get_queryset(self):
        """ Queryset function for manage booking search """
        query = self.request.GET.get('q')
        dates = self.request.GET.get('d')
        if query:
            return Booking.objects.filter(id=query)
        if dates:
            return Booking.objects.filter(booking_date=dates)
        if self.request.user.is_staff:
            # returns all bookings with date greater than yesterday
            return Booking.objects.filter(
                booking_date__gt=(date.today()-timedelta(days=1))
                )
        else:
            # returns all bookings for logged in customer
            # with date greater than yesterday
            return Booking.objects.filter(
                booking_name=self.request.user,
                booking_date__gt=(date.today()-timedelta(days=1))
                )


class EditBookingView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to provide a Form to the user
    to edit a booking
    """
    form_class = BookingForm
    template_name = 'booking/edit_booking.html'
    success_url = "/booking/managebookings"
    model = Booking

    def form_valid(self, form):
        """
        Before form submission, run capacity checks and
        assign to table with lowest capacity
        """
        date = form.cleaned_data['booking_date']
        time = form.cleaned_data['booking_slot']
        guests = form.cleaned_data['number_of_guests']

        # Filter tables with capacity greater than or equal
        # to the number of guests (using __gte method)
        available_table = list(Table.objects.filter(
            capacity__gte=guests
        ))
        
        # Filter tables with the requested date
        bookings_on_requested_date = Booking.objects.filter(
            booking_date=date, booking_slot=time)
        
        # Iterate over bookings and remove table from bookings
        for booking in bookings_on_requested_date:
            for table in available_table:
                if table.number == booking.booking_table.number:
                    available_table.remove(table)
                    break

        # Iterate over tables with capacity and assign lowest
        # capacity table
        if available_table:
            lowest_capacity_table = available_table[0]
            for table in available_table:
                if table.capacity < lowest_capacity_table.capacity:
                    lowest_capacity_table = table
            form.instance.booking_table = lowest_capacity_table

        messages.success(
            self.request,
            f'Successfully updated booking for {guests} guests on {date}'
        )
        return super(EditBookingView, self).form_valid(form)

    def test_func(self):
        """ Test user is staff or throw 403 """
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().booking_name


class DeleteBookingView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to delete a booking """
    model = Booking
    success_url = "/booking/managebookings"

    def form_valid(self, form):
        """ Display toast message on form success """
        messages.success(
            self.request,
            'Successfully deleted booking'
        )
        return super(DeleteBookingView, self).form_valid(form)

    def test_func(self):
        """ Test user is staff else throw 403 """
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().booking_name