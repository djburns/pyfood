from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=30)
    postcode = models.CharField(max_length=8)

class Vendor(models.Model):
    name = models.CharField(max_length=30)

class Order(models.Model):
    event = models.ForeignKey(Event)
    vendor = models.ForeignKey(Vendor)
    organiser = models.ForeignKey(User)
    closing_date = models.DateField()
