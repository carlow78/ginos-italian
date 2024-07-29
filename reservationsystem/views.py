from django.views.generic import CreateView

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
    success_url = '/bookings/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBooking, self).form_valid(form)





