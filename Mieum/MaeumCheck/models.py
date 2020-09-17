from django.db import models

# Create your models here.

class Meeting(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Place(Meeting):
    maxPeople = models.IntegerField()
    currentPeople = models.IntegerField()
    congestion = models.IntegerField()

class Meeting_Visit(models.Model):
    visited_at = models.DateTimeField(auto_now_add=True)
    visiter = models.CharField(max_length=50)
    meeting = models.ForeignKey(Meeting,on_delete=models.PROTECT)

class Place_Visit(models.Model):
    visited_at = models.DateTimeField(auto_now_add=True)
    visiter = models.CharField(max_length=50)
    place = models.ForeignKey(Place,on_delete=models.PROTECT)