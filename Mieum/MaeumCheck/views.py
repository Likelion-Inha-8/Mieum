from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def home(request):
    return render(request,'home.html')

def congestionsearch(request):
    data = request.POST.get('data')
    places = Place.objects.filter(name__icontains=data)
    return render(request, 'congestionsearch.html',{'places':places})

def SetPlace(request):
    return render(request, 'setPlace.html')

def SavePlace(request):
    if request.method == 'POST':
        place = Place()
        place.name = request.POST.get('name')
        place.owner = request.user
        place.maxPeople = request.POST.get('maxpeople')
        place.currentPeople = 0
        place.congestion = 0
        place.address = request.POST.get('address')
        place.save()
    return redirect('home')

def QRShow(request,id):
    place = get_object_or_404(Place,pk=id)
    return render(request, 'QR.html',{'place':place})


def MyPage(request):
    pass