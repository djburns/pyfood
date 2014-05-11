from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=30)
    postcode = models.CharField(max_length=8,blank=True)
    vendors = models.ManyToManyField(Vendor)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class ItemGroup(models.Model):
    vendor = models.ForeignKey(Vendor)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return '{0} - {1}'.format(
            self.vendor.name,
            self.name)


class Item(models.Model):
    item_group = models.ForeignKey(ItemGroup)
    item = models.ForeignKey(
        'self',
        related_name='+',
        blank=True,
        null=True)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True)

    def __unicode__(self):
        if self.item:
            return '{0} - {1}'.format(self.item.name, self.name)
        return self.name


class Order(models.Model):
    event = models.ForeignKey(Event)
    vendor = models.ForeignKey(Vendor)
    organiser = models.ForeignKey(User)
    closing_datetime = models.DateTimeField()

    def __unicode__(self):
        return '{0} - {1} ({2})'.format(
            self.event,
            self.vendor,
            self.closing_datetime)


class UserOrder(models.Model):
    user = models.ForeignKey(User)
    order = models.ForeignKey(Order)

    def __unicode__(self):
        return '{0} ({1})'.format(
            self.user,
            self.order)


class UserOrderItem(models.Model):
    user_order = models.ForeignKey(UserOrder)
    item = models.ForeignKey(Item)
    comment = models.TextField()

    def __unicode__(self):
        return self.item
