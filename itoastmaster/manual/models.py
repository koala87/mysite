from __future__ import unicode_literals

from django.db import models
    
    
    # Create your models here.
class Objective(models.Model):
    description = models.TextField()
    
    def __str__(self):              # __unicode__ on Python 2
        return self.description
    
    
class Manual(models.Model):
    kind = models.CharField(max_length=10)
    level = models.IntegerField()
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    ltime = models.FloatField(blank=True, null=True)
    mtime = models.FloatField(blank=True, null=True)
    obj = models.ManyToManyField(Objective)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.title
    

    
    
    

