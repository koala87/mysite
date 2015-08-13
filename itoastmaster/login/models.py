from __future__ import unicode_literals

from django.db import models
from club.models import Club 

# Create your models here.
class Province1(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=100)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    
    
class School(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=100)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    
class Province(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=100)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    
    
class City(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=100)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    

class User(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.email+self.password


class UserInfo(models.Model):
    # main key
    email = models.CharField(max_length=200)
    
    # basic
    name = models.CharField(max_length=100)
    portrait = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=8, blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    lovebridge = models.BooleanField(blank=True)
    hometown = models.TextField(blank=True, null=True)
    school = models.TextField(blank=True, null=True)
    
    # toastmaster
    club = models.ForeignKey(Club, blank=True, null=True)
    join_dt = models.DateField(blank=True, null=True)
    progress = models.TextField(blank=True, null=True)
    positions = models.TextField(blank=True, null=True)
    
    # self
    interest = models.TextField(blank=True, null=True)
    self_introduction = models.TextField(blank=True, null=True)
    word = models.TextField(blank=True, null=True)
    

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    