from django.conf import settings
from django.db import models

# Create your models here.

STAR_CHOICES = (
    (1 , 1),
    (2 , 2),
    (3 , 3),
    (4 , 4),
    (5 , 5)
)


class Hotel(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    star = models.IntegerField(max_length=1, choices=STAR_CHOICES)
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.title


class HotelImage(models.Model):
    img = models.ImageField('hotels/')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=False)
    booked = models.BooleanField(default=False)

