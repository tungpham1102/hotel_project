from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from .forms import CheckoutForm
from .models import Hotel, Booking, Checkout, BookHotel


# Create your views here.


class HomeView(ListView):
    model = Hotel
    template_name = 'hotels/home.html'


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotels/hotel.html'


class BookDetailView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            booking = Booking.objects.get(user=self.request.user, booked=False)
            context = {
                'object': booking
            }
            return render(self.request, 'hotels/bookdetail.html', context)
        except ObjectDoesNotExist:
            return redirect('/')


class CheckoutView(View):
    def get(self, *args, **kwargs):
        hotel = Hotel.objects.all()
        form = CheckoutForm()
        context = {
            'hotel': hotel,
            'form': form
        }
        return render(self.request, 'hotels/checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            print('chay vao day khong')
            book = Booking.objects.get(user=self.request.user, booked = False)
            if form.is_valid():
                print('the con day')
                print(form.cleaned_data)
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                birthday = form.cleaned_data.get('birthday')
                gender = form.cleaned_data.get('gender')
                phone = form.cleaned_data.get('phone')
                checkout = Checkout(
                    user = self.request.user,
                    first_name = first_name,
                    last_name = last_name,
                    birthday = birthday,
                    gender = gender,
                    phone = phone,
                )
                checkout.save()
                book.checkout = checkout
                messages.info(self.request, 'you complete booking')
                book.save()
            return redirect('hotels:home')
        except ObjectDoesNotExist:
            return redirect('hotels:checkout')


@login_required
def add_booking(request, slug):
    hotel = get_object_or_404(Hotel, slug = slug)
    book_hotel, created = BookHotel.objects.get_or_create(
        hotel = hotel,
        user = request.user,
        booked = False
    )
    booking_qs = Booking.objects.filter(
        user = request.user,
        booked = False
    )
    if booking_qs.exists():
        booking = booking_qs[0]
        if booking.hotels.filter(hotel__slug=hotel.slug).exists():
            book_hotel.save()
            return redirect('hotels:book-detail')
        else:
            booking.hotels.add(book_hotel)
            return redirect('hotels:book-detail')
    else:
        booking_date = timezone.now()
        booking = Booking.objects.create(user=request.user, booking_date=booking_date)
        booking.hotels.add(book_hotel)
    return redirect('hotels:book-detail')


@login_required
def remove_booking(request, slug):
    hotel = get_object_or_404(Hotel, slug=slug)
    booking_qs = Booking.objects.filter(
        user=request.user,
        booked = False
    )
    if booking_qs.exists():
        booking = booking_qs[0]
        # check if the order item is in the order
        if booking.hotels.filter(hotel__slug = hotel.slug).exists():
            book_hotel = BookHotel.objects.filter(
                hotel = hotel,
                user = request.user,
                booked = False
            )[0]
            booking.hotels.remove(book_hotel)
            return redirect('hotels:hotel', slug=slug)
        else:
            return redirect('hotels:hotel', slug=slug)
    else:
        return redirect('hotels:hotel', slug=slug)


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)