from django.conf.urls import url
from django.urls import path
from .views import (
    HomeView,
    HotelDetailView,
    BookDetailView,
    CheckoutView,
    add_booking,
    remove_booking,
    validate_username,
)

app_name = 'hotels'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('hotel/<slug>', HotelDetailView.as_view(), name='hotel'),
    path('book-detail', BookDetailView.as_view(), name='book-detail'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('add-booking/<slug>/', add_booking, name='add-booking'),
    path('remove-booking/<slug>/', remove_booking, name='remove-booking'),
    path('validate_username', validate_username, name='validate_username'),
]
