from django.db import models
from django.conf import settings

# Create your models here.

class Space(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class Meeting(Space):
    Start_Time = models.TimeField()
    End_Time = models.TimeField()

class Place(Space):
    address = models.CharField(max_length=100)
    maxPeople = models.IntegerField()
    currentPeople = models.IntegerField()
    congestion = models.IntegerField()

class Meeting_Visit(models.Model):
    visited_at = models.TimeField(auto_now_add=True)
    visiter = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting,on_delete=models.CASCADE)

class Place_Visit(models.Model):
    visited_at = models.DateTimeField(auto_now_add=True)
    visiter = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    place = models.ForeignKey(Place,on_delete=models.CASCADE)