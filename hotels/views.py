from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Hotel

# Create your views here.


class HomeView(ListView):
    model = Hotel
    template_name = 'hotels/home.html'


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotels/hotel.html'