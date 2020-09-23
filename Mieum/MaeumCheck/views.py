from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import qrcode
from django.http import HttpResponse
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    name = 0
    if request.user.is_authenticated:
        socialUser = get_object_or_404(SocialAccount, user=request.user)
        name = socialUser.extra_data['name']
    return render(request,'home.html',{'name':name})

def congestionsearch(request):
    data = request.POST.get('data')
    places = Place.objects.filter(name__icontains=data)
    return render(request, 'congestionsearch.html',{'places':places, 'data':data})

@login_required
def SetPlace(request):
    return render(request, 'setPlace.html')

@login_required
def SetMeeting(request):
    return render(request, 'setMeeting.html')

@login_required
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
    return redirect('MyPlaceList')

@login_required
def SaveMeeting(request):
    if request.method == 'POST':
        meeting = Meeting()
        meeting.name = request.POST.get('name')
        meeting.Start_Time = request.POST.get('start')
        meeting.End_Time = request.POST.get('end')
        meeting.owner = request.user
        meeting.save()
    return redirect('MyMeetingList')

@login_required
def MyPlaceList(request):
    places = Place.objects.filter(owner=request.user).order_by('-id')
    return render(request, 'MyPlaceList.html',{'places':places})

@login_required
def MyMeetingList(request):
    meetings = Meeting.objects.filter(owner=request.user).order_by('-id')
    return render(request, 'MyMeetingList.html',{'meetings':meetings})

@login_required
def PlaceQRShow(request,id):
    place = get_object_or_404(Place,pk=id)
    return render(request, 'PlaceQR.html',{'place':place})

@login_required
def MeetingQRShow(request,id):
    meeting = get_object_or_404(Meeting,pk=id)
    return render(request, 'MeetingQR.html',{'meeting':meeting})

@login_required
def MyVisitedPlace(request):
    visitedplaces = Place_Visit.objects.filter(visiter=request.user).order_by('-visited_at')
    return render(request, 'MyVisitedPlace.html',{'visitedplaces':visitedplaces})

def MyVisitedMeeting(request):
    visitedmeetings = Meeting_Visit.objects.filter(visiter=request.user).order_by('-visited_at')
    return render(request, 'MyVisitedMeeting.html',{'visitedmeetings':visitedmeetings})

@login_required
def PlacegenQR(request, code_id):
    url = 'http://127.0.0.1:8000/placeqrshow/' + str(code_id) + '/comments/'
    img = qrcode.make(url)
    response = HttpResponse(content_type="image/png")
    img = img.save(response, "png") # 사진을 만든다 -> 이름을 붙여줄 주소가 필요하다
    return (response)

@login_required
def PlaceExitgenQR(request, code_id):
    url = 'http://127.0.0.1:8000/placeqrshow/' + str(code_id) + '/exit/'
    img = qrcode.make(url)
    response = HttpResponse(content_type="image/png")
    img = img.save(response, "png") # 사진을 만든다 -> 이름을 붙여줄 주소가 필요하다
    return (response)

@login_required
def MeetinggenQR(request, code_id):
    url = 'http://127.0.0.1:8000/meetingqrshow/' + str(code_id) + '/comments/'
    img = qrcode.make(url)
    response = HttpResponse(content_type="image/png")
    img = img.save(response, "png") # 사진을 만든다 -> 이름을 붙여줄 주소가 필요하다
    return (response)

@login_required
def PlaceSaveComplete(request,code_id):
    visit_write = Place_Visit()
    visit_write.visiter = request.user
    visit_write.place = get_object_or_404(Place,pk=code_id)
    aPlace = get_object_or_404(Place,pk=code_id)
    a = int(aPlace.currentPeople)
    if a < int(aPlace.maxPeople):
        a = a + 1
        aPlace.currentPeople = a
    if a > int(int(aPlace.maxPeople)/3):
        if a > 2*int(int(aPlace.maxPeople)/3):
            aPlace.congestion = 2
        else:
            aPlace.congestion = 1
    else:
        aPlace.congetsion = 0
    visit_write.save()
    aPlace.save()
    return render(request,'complete.html')

@login_required
def MeetingSaveComplete(request,code_id):
    visit_write = Meeting_Visit()
    visit_write.visiter = request.user
    visit_write.meeting = get_object_or_404(Meeting,pk=code_id)
    visit_write.save()
    if visit_write.visited_at > visit_write.meeting.End_Time:
        meeting = get_object_or_404(Meeting,pk=code_id)
        meeting.delete()
        return render(request, 'delete.html')
    return render(request,'complete.html')

def QRCodeImg(request,code_id):
    return (genQR(code_id))

def Getout(request,code_id):
    outPlace = get_object_or_404(Place,pk=code_id)
    a = int(outPlace.currentPeople)
    if a > 0:
        a = a - 1
        outPlace.currentPeople = a
    if a > int(int(outPlace.maxPeople)/3):
        if a > 2*int(int(outPlace.maxPeople)/3):
            outPlace.congestion = 2
        else:
            outPlace.congestion = 1
    else:
        outPlace.congestion = 0
    print(outPlace.currentPeople)
    outPlace.save()
    return render(request,'complete.html')

def DeletePlace(request,id):
    place = get_object_or_404(Place,pk=id)
    place.delete()
    return render(request,'delete.html')

def DeleteMeeting(request,id):
    meeting = get_object_or_404(Meeting,pk=id)
    meeting.delete()
    return render(request,'delete.html')