from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ReservationSystem
from .forms import BookingForm
from django.contrib import messages


class AddBooking(LoginRequiredMixin, CreateView):

    """
    Add booking view
    """
    template_name = 'bookings/add_booking.html'
    model = ReservationSystem
    form_class = BookingForm
    success_url = 'bookings/booking_success/'

    def add_booking (self, request):
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
    model = ReservationSystem
    template_name = 'bookings/view_reservation.html'  # Template to display user bookings
    context_object_name = 'bookings'  # Context variable to access bookings in the template folder

    def get_queryset(self):
        """
        Override to filter bookings by the logged-in user.
        """
        return ReservationSystem.objects.filter(user=self.request.user)

class EditBooking(LoginRequiredMixin, UpdateView):

    template_name = 'bookings/edit_reservation.html'
    model = ReservationSystem
    form_class = BookingForm
    success_url = '../booking_success'

    def get_object(self, queryset=None):

        booking_id = self.kwargs.get('pk')
        return get_object_or_404(ReservationSystem, pk=booking_id, user=self.request.user)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Booking has been updated successfully.')
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, 'Booking has not been updated. Please check inputted details')
        return self.render_to_response({'form': form})

    




       