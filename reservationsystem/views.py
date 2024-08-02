from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import reservationsystem
from .forms import BookingForm




class AddBooking(LoginRequiredMixin, CreateView):

    """
    Add booking view
    """
    template_name = 'bookings/add_booking.html'
    model = reservationsystem
    form_class = BookingForm
    success_url = 'bookings/booking_success/'

    def booking (self, request):
        return render(request, 'add_booking.html')

    def post(self, request):
        
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return render(request, 'bookings/booking_success.html')
        else:
            messages.error(request, 'Booking not completed, please check your booking information')

        return render(request, 'bookings.html',{
                'form': form
                }
                )    


class BookingSuccess(generic.DetailView):
    """
    Renders the Thank You page in the browser
    """
    template_name = 'booking_success.html'

    def get(self, request):
        return render(request, 'booking_success.html')


class UserBookings(LoginRequiredMixin, ListView):
    """
    View to display the bookings for the logged-in user.
    """
    model = reservationsystem
    template_name = 'bookings/view_reservation.html'  # Template to display user bookings
    context_object_name = 'bookings'  # Context variable to access bookings in the template

    def get_queryset(self):
        """
        Override to filter bookings by the logged-in user.
        """
        return reservationsystem.objects.filter(user=self.request.user)
       