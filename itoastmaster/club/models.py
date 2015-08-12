from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Club(models.Model):

    name = models.CharField(max_length=64)
    time = models.TextField(blank=True, null=True)
    week = models.IntegerField(blank=True, null=True)
    addr = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    geo_longitude = models.FloatField(blank=True, null=True)
    geo_latitude = models.FloatField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    zones_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name