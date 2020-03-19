from django.urls import path
from .views import (
    HomeView,
    HotelDetailView
    )

app_name = 'hotels'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('hotel/<slug>', HotelDetailView.as_view(), name='hotel'),
]