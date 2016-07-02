from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    phone = models.CharField(max_length=32)

    def __unicode__(self):
        return self.user.username


class Fang(models.Model):
    user_profile = models.ForeignKey('zufang.userprofile', related_name='fangs')
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
    zipcode = models.CharField(max_length=16)
    street = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=32,
        null=True,
        blank=True,
    )
    state = models.CharField(
        max_length=32,
        null=True,
        blank=True,
    )
    country = models.CharField(
        max_length=32,
        default='United States',
    )
    lat = models.FloatField(
        blank=True,
        null=True,
    )
    lon = models.FloatField(
        blank=True,
        null=True,
    )
    active = models.BooleanField(default=True)


    def __unicode__(self):
        return '%s: %s %s - num_bathroom: %s' % (
            self.id,
            ['number bedroom', 'studio'][self.is_studio],
            self.num_bedroom,
            self.num_bathroom,
        )


class Picture(models.Model):
    fang = models.ForeignKey('zufang.Fang', related_name='pictures')
    source = models.URLField()
    name = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return '%s - %s' % (self.fang.id, self.name)
