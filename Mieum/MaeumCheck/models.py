from django.db import models
from django.conf import settings

# Create your models here.

class Meeting(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

class Place(Meeting):
    address = models.CharField(max_length=100)
    maxPeople = models.IntegerField()
    currentPeople = models.IntegerField()
    congestion = models.IntegerField()

class Meeting_Visit(models.Model):
    visited_at = models.DateTimeField(auto_now_add=True)
    visiter = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    meeting = models.ForeignKey(Meeting,on_delete=models.PROTECT)

class Place_Visit(models.Model):
    visited_at = models.DateTimeField(auto_now_add=True)
    visiter = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    place = models.ForeignKey(Place,on_delete=models.PROTECT)