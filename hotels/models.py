from django.conf import settings
from django.db import models
from django.forms import ModelForm
from django_countries.fields import CountryField

# Create your models here.
from django.urls import reverse

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
    star = models.IntegerField(choices=STAR_CHOICES)
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('hotels:hotel', kwargs={
            'slug': self.slug
        })

    def get_checkout_url(self):
        return reverse('hotels:checkout', kwargs={
            'slug': self.slug
        })

    def get_add_booking_url(self):
        return reverse('hotels:add-booking', kwargs={
            'slug': self.slug
        })


class HotelImage(models.Model):
    img = models.ImageField(upload_to='static/media/imghotel/', default='default.jpg')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.hotel.title} - {self.featured}'


class BookHotel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    booked = models.BooleanField(default=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.hotel.title}'

    def get_total_hotel_price(self):
        return self.hotel.price

    def get_total_hotel_discount_price(self):
        return self.hotel.discount_price

    def get_amount_saved(self):
        return self.get_total_hotel_price() - self.get_total_hotel_discount_price()

    def get_final_price(self):
        if self.hotel.discount_price:
            return self.get_total_hotel_discount_price()
        return self.get_total_hotel_price()


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hotels = models.ManyToManyField(BookHotel)
    booking_date = models.DateTimeField()
    booked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for book_hotel in self.hotels.all():
            total += book_hotel.get_final_price()
        return total


class Checkout(models.Model):

    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, help_text='first_name')
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    phone = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class CheckoutForm(ModelForm):
    class Meta:
        model = Checkout
        fields = '__all__'



