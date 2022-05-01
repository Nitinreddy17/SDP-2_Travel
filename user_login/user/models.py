from django.contrib.auth.models import User
from django.db import models


class Buses(models.Model):
    travels = models.CharField(max_length=50, blank=False)
    departure_timeHours = models.CharField(max_length=2, blank=False)
    departure_timeMinutes = models.CharField(max_length=2, blank=False)
    departure_palce = models.CharField(max_length=50, blank=False)
    arrival_timeHours = models.CharField(max_length=2, blank=False)
    arrival_timeMinutes = models.CharField(max_length=2, blank=False)
    arrival_place = models.CharField(max_length=50, blank=False)
    duration = models.CharField(max_length=25, blank=False)
    fare = models.CharField(max_length=20, blank=False)
    seats_available = models.IntegerField(blank=False)
    ac_sleeper = models.CharField(max_length=20, blank=False)
    bus_num = models.CharField(max_length=15, blank=False, default="AP04BN5444")
    date = models.CharField(max_length=10, blank=False, default="01/01/2021")
    day = models.CharField(max_length=10, blank=False, default="Friday")
    one = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    two = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    three = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    four = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    five = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    six = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    seven = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    eight = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    nine = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    ten = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    elven = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    twelve = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    thirtn = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    fouthn = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    fivethn = models.CharField(max_length=10, blank=False, default="#DDF4EC")
    sixthn = models.CharField(max_length=10, blank=False, default="#DDF4EC")

    class Meta:
        db_table = "buses_table"

    class Flights(models.Model):
        flight = models.CharField(max_length=50, blank=False)
        departure_timeHours = models.CharField(max_length=2, blank=False)
        departure_timeMinutes = models.CharField(max_length=2, blank=False)
        departure_palce = models.CharField(max_length=50, blank=False)
        arrival_timeHours = models.CharField(max_length=2, blank=False)
        arrival_timeMinutes = models.CharField(max_length=2, blank=False)
        arrival_place = models.CharField(max_length=50, blank=False)
        duration = models.CharField(max_length=25, blank=False)
        fare = models.CharField(max_length=20, blank=False)
        seats_available = models.IntegerField(blank=False)
        date = models.CharField(max_length=10, blank=False, default="01/04/2022")
        day = models.CharField(max_length=10, blank=False, default="Monday")

        class Meta:
            db_table = "flights_table"


    class Tours(models.Model):
        location = models.CharField(max_length=100, blank=False)
        touristplces_covered = models.CharField(max_length=500, blank=False)
        hotel = models.CharField(max_length=150, blank=False)
        cost = models.CharField(max_length=100, blank=False)

        class Meta:
           db_table = "Tours"