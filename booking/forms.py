from datetime import datetime
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django import forms
from .models import Table, Booking

# Form code taken mostly from Mentor Greg McGirr (Sizzle & Steak)
class BookingForm(forms.ModelForm):
    """
    Form for creating and updating bookings.
    """
    class Meta:
        """
        This class sets fields and labels for the form.
        """
        model = Booking
        fields = [
            'booking_name', 'booking_date', 'booking_size', 
            'booking_slot', 'package', 'allergies', 'special'
        ]
        labels = {
            'booking_name': 'Name',
            'booking_date': 'Date',
            'booking_size': 'Group Size',
            'booking_slot': 'Time-slot',
            'package': 'Package',
            'allergies': 'Does you party have any allergies?',
            'special': 'Use keywords to specify any special requirements',
        }
        booking_date = forms.DateField(help_text="Date must be set in the future")

    def clean(self):
        """
        Get form data and clean, check capacity and
        throw errors when tables not available
        """
        date = self.cleaned_data['booking_date']
        time = self.cleaned_data['booking_slot']
        guests = self.cleaned_data['booking_size']

        table_booked = None

        # Try and get object, as needed for update validation
        # pass error if on create
        try:
            table_booked = Table.objects.get(id=self.instance.booking_table.id)
        except ObjectDoesNotExist:
            pass

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

        # Add booked table to list of tables
        if table_booked is not None:
            if table_booked.capacity >= guests:
                available_table.append(table_booked)

        # Throw validation errors on form
        if date < datetime.today().date():
            raise ValidationError(
                'Invalid date - Booking cannot be in the past')
        if guests > 8:
            raise ValidationError(
                'Maximum group size cannot exceed 8 people')
        if table_booked is not None:
            if not available_table and table_booked.capacity < guests:
                raise ValidationError(
                    'Sorry, we do not have a table' +
                    ' available for that amount of guests'
                )
        if not available_table:
            raise ValidationError('No tables available for this date and time')
        


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Date field attributes - links datepicker calendar, makes field
        # non-editble by direct input and sets the current date as a
        # default value to avoid form submission errors.
        self.fields['booking_date'].widget.attrs['class'] = 'datepicker'
        self.fields['booking_date'].widget.attrs['value'] = datetime.now().date()
        self.fields['booking_date'].widget.attrs['autocomplete'] = 'off'
        self.fields['booking_date'].widget.attrs['readonly'] = 'readonly'
        # Booking-size field attributes - sets min and max values for integer field
        self.fields['booking_size'].widget.attrs['min'] = 1
        self.fields['booking_size'].widget.attrs['max'] = 8
        # Package field attributes
        self.fields['package'].required = False
        self.fields['package'].widget.attrs['empty_label'] = None
        self.fields['allergies'].widget.attrs['class'] = 'allergy-label'
        self.fields['special'].widget.attrs['class'] = 'special-label'
        self.fields['special'].widget.attrs['placeholder'] = 'e.g Wheelchair access'
        self.fields['special'].required = False