from django.db import models


class Bookings(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    num_of_guests = models.IntegerField()
    Date = models.DateField()
    time = models.TimeField()


def __str__(self):
    return self.name
