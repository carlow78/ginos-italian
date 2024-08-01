from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import reservationsystem
from .forms import BookingForm

class Reservation(generic.DetailView):
    

    template_name = 'bookings/view_reservation.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            bookings = reservationsystem.objects.filter(user=request.user)

            return render(request, 'bookings/view_reservation.html', {
                'bookings': bookings
            }
            )
        else:
            return redirect('account_login')



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

       