from django.conf import settings
from django.db import models

RATE_CHOICES = [
    (1, '1 - Trash'),
    (2, '2- Horrible'),
    (3, '3- Terrible'),
    (4, '4- Bad'),
    (5, '5- OK'),
    (6, '6- Rideable'),
    (7, '7- Good'),
    (8, '8- Very good'),
    (9, '9- Perfect'),
    (10, '10- Best'),

]

HotelChoices = [
    ('Pan_Pacific_Sonargoan', 'Pan Pacific Sonargoan'),
    ('Radisson_Blu', 'Radisson Blu'),
    ('Hotel De Meridian', 'Hotel De Meridian'),
    ('Grand Plaza Hotel', 'Grand Plaza Hotel'),
    ('Empyrean Hotel', 'Empyrean Hotel'),
    ('The Raintree Dhaka', 'The Raintree Dhaka')
]

ResturantChoices = [
    ('Sultans Dine', 'Sultans Dine'),
    ('Pizza Hut', 'Pizza Hut'),
    ('Chillox', 'Chillox'),
    ('Khanas', 'Khanas'),
    ('Burger King', 'Burger King'),
    ('Kacchi Vai', 'Kacchi Vai')
]

PlaceChoices = [
    ('Dhaka', 'Dhaka'),
    ('Cox_Bazar', 'Cox Bazar'),
    ('Sylhet', 'Sylhet'),
    ('Cumilla', 'Cumilla'),
    ('Gazipur', 'Gazipur'),
    ('Rajshahi', 'Rajshahi')
]


class HotelReview(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    hotelName = models.CharField(choices=HotelChoices, max_length=100, default=None, null=True)
    review = models.TextField(max_length=3000, blank=True)
    rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class ResturantReview(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    resturantName = models.CharField(choices=ResturantChoices, max_length=100, default=None, null=True)
    review = models.TextField(max_length=3000, blank=True)
    rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class PlaceReview(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    placeName = models.CharField(choices=PlaceChoices, max_length=100, default=None, null=True)
    review = models.TextField(max_length=3000, blank=True)
    rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class HotelReservation(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=30)
    user_phone = models.CharField(max_length=20)
    checkin_date = models.CharField(max_length=20)
    checkout_date = models.CharField(max_length=20)
    hotel_name = models.CharField(max_length=20)
    room_number = models.CharField(max_length=20)
    room_type = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.DO_NOTHING)


class RoomModel(models.Model):
    roomtype = models.CharField(max_length=20)
    beds = models.CharField(max_length=20)
    baths = models.CharField(max_length=20)
    slug = models.SlugField()
    guests = models.IntegerField()
    amenities = models.TextField(max_length=3000, blank=True)
    facilities = models.TextField(max_length=3000, blank=True)
    room_Img1 = models.ImageField(blank=True, null=True)
    room_Img2 = models.ImageField(blank=True, null=True)
    room_Img3 = models.ImageField(blank=True, null=True)


class Place(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(max_length=3000, blank=True)
    route = models.TextField(max_length=3000, blank=True)
    map_link = models.TextField(max_length=3000, blank=True)
    place_Img1 = models.ImageField(blank=True, null=True)
    place_Img2 = models.ImageField(blank=True, null=True)
    place_Img3 = models.ImageField(blank=True, null=True)
