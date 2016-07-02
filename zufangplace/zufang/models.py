from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.username


class Fang(models.Model):
    user_profile = models.ManyToManyField(UserProfile)
    is_studio = models.BooleanField(default=False)
    num_bedroom = models.IntegerField(
        default=None,
        null=True,
        blank=True,
    )
    num_bathroom = models.IntegerField()
    date_avaialable = models.DateTimeField(auto_now_add=True)
    price_rent = models.FloatField(
        default=None,
        null=True,
        blank=True,
    )
    price_buy = models.FloatField(
        default=None,
        null=True,
        blank=True,
    )
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s %s - num_bathroom: %s' % (['number bedroom', 'studio'][self.is_studio], self.num_bedroom, self.num_bathroom)


class Address(models.Model):
    fang = models.ForeignKey(Fang)
    zipcode = models.CharField(max_length=16)
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    country = models.CharField(
        max_length=32,
        default='United States',
    )
    lat = models.FloatField()
    lon = models.FloatField()


class PhoneNumber(models.Model):
    number = models.CharField(max_length=32)
    user_profile = models.ForeignKey(UserProfile)
    is_primary = models.BooleanField(default=False)
