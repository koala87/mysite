from django.db import models

# Create your models here.

# TBD: create model

class Member(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    birth = models.CharField(max_length=50)
    hometown = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    mayer = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    interest = models.CharField(max_length=50)
    available = models.CharField(max_length=50) 
    member = models.CharField(max_length=50) 

    #join_date = models.CharField(max_length=50)
    #leave_date = models.CharField(max_length=50)
    # club
    #club = models.CharField(max_length=50) # class club
    # joined meeting
    #meetings = models.CharField(max_length=50) # class meeting
    # taked roles
    #roles = models.CharField(max_length=50) # roles

class Meeting(models.Model):
    date = models.DateField()
    place = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    TME = models.CharField(max_length=50)
    TTM = models.CharField(max_length=50)
    TTE = models.CharField(max_length=50)
    SP1 = models.CharField(max_length=50) # sp should be a class
    SP2 = models.CharField(max_length=50)
    SP3 = models.CharField(max_length=50)
    IE1 = models.CharField(max_length=50)
    IE2 = models.CharField(max_length=50)
    IE3 = models.CharField(max_length=50)
    GE = models.CharField(max_length=50)
    TIMER = models.CharField(max_length=50)
    GRAM = models.CharField(max_length=50)
    AH = models.CharField(max_length=50)

#class Club(models.Model):
#   People
#   Meeting
#   Date
#   Place
#   Traffic
#   Logo
#   ...

#class Role(models.Model)
#   name
#   script

#class Speech(models.Model)
#    meeting 
#    speaker 
#    titile
#    Manal 
#    ie
#    comments 
 
#class Manal(models.Model)
#    CC/CL/AC?   
#    time?
#    objective
