from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import qrcode
from django.http import HttpResponse
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount


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

def genQR(request, code_id):
    url = 'qrshow/' + str(code_id) + '/comment/'
    img = qrcode.make(url)
    response = HttpResponse(content_type="image/png")
    img = img.save(response, "png") # 사진을 만든다 -> 이름을 붙여줄 주소가 필요하다
    return (response)

def SaveComplete(request,id):
    visit_write = Place_Visit()
    visit_write.visiter = request.user
    visit_write.save()
    return render(request,'complete.html')

def QRCodeImg(request,code_id):
    return (genQR(code_id))