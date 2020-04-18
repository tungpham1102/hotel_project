from django.contrib import admin
from .models import Hotel, HotelImage, Booking,BookHotel

# Register your models here.


class HotelAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'price', 'star', 'slug']
    prepopulated_fields = {"slug":("title", )}

    class Meta:
        model = Hotel


admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelImage)
admin.site.register(Booking)
admin.site.register(BookHotel)