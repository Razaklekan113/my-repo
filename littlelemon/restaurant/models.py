from django.db import models

# Create your models here.
class BookingTable(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(6)
    bookingdate = models.DateTimeField()

class MenuTable(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    inventory = models.IntegerField(5)
    