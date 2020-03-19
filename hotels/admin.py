from django.contrib import admin
from .models import Hotel, HotelImage, Booking

# Register your models here.


admin.site.register(Hotel)
admin.site.register(HotelImage)
admin.site.register(Booking)