from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import ReservationSystem
from .forms import BookingForm
from django.contrib import messages

class Home(generic.DetailView):
    """
    Displays the Index page in the browser
    """
    def index(request):
        return render(request, 'index.html')

class Menu(generic.DetailView):
    """
     Displays the Menu page in the browser
    """
    def get(self, request):
        return render(request, 'bookings/menu.html')
    

class AddBooking(LoginRequiredMixin, CreateView):

    """
    Add booking view. Allows the user to add a booking,
    All fields must be filled in except for comment field.
    When they have successfully added a booking they are
    brought to a successful booking page "booking_success"

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


class BookingSuccess(generic.DetailView):
    """
    Renders the Booking Success page in the browser
    """
    template_name = 'booking_success.html'

    def get(self, request):
        return render(request, 'booking_success.html')


class UserBookings(LoginRequiredMixin, ListView):
    """
    View to display the bookings for the logged-in user.
    """
    model = ReservationSystem
    template_name = 'bookings/view_reservation.html' 
    context_object_name = 'bookings'  

    def get_queryset(self):
        """
        Override to filter bookings by the logged-in user.
        """
        return ReservationSystem.objects.filter(user=self.request.user)

class EditBooking(LoginRequiredMixin, generic.UpdateView):

    """
    Allows the logged in user (LoginRequiredMixin) to edit their 
    reservation(s).
    Using the booking_id as the primary key.
    When they have changed their reservation they are brought back
    to their list of reservation page "view_reservation".
    """

    template_name = 'bookings/edit_reservation.html'
    model = ReservationSystem
    form_class = BookingForm
    success_url = '../view_reservation'
    

    def get_object(self, queryset=None):

        booking_id = self.kwargs.get('pk')
        return get_object_or_404(ReservationSystem, pk=booking_id, user=self.request.user)

    def form_valid(self, form):
        
        form.save()
        return redirect(self.success_url)

    def form_invalid(self, form):
        
        return render(self.request, self.template_name, {'form': form})


class DeleteBooking(LoginRequiredMixin, generic.DeleteView):
    """
    Allows the logged in user to delete a reservation.
    When they click on the "delete reservation" button. 
    They will be brought to "delete reservation" where they need to click on the
     "Delete Confirm" button - deleting booking from the db.
    The user is then returned to their list of reservation(s)
    "view_reservation" which shows their other reservation(s) (if any).
    """


    model = ReservationSystem
    template_name = 'bookings/delete_reservation.html'
    success_url = '/reservationsystem/view_reservation'

    def get_object(self, queryset=None):
        booking_id = self.kwargs.get('pk')
        return get_object_or_404(ReservationSystem, pk=booking_id, user=self.request.user)


    

       