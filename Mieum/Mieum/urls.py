"""Mieum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import MaeumCheck.views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',MaeumCheck.views.home,name='home'),
    path('search/',MaeumCheck.views.congestionsearch,name='congestionsearch'),
    path('setplace/',MaeumCheck.views.SetPlace,name='SetPlace'),
    path('setmeeting/',MaeumCheck.views.SetMeeting,name='SetMeeting'),
    path('saveplace/',MaeumCheck.views.SavePlace,name='SavePlace'),
    path('savemeeting/',MaeumCheck.views.SaveMeeting,name='SaveMeeting'),
    path('placeqrshow/<int:id>',MaeumCheck.views.PlaceQRShow,name='PlaceQRShow'),
    path('meetingqrshow/<int:id>',MaeumCheck.views.MeetingQRShow,name='MeetingQRShow'),
    path('myvisitedplace/',MaeumCheck.views.MyVisitedPlace,name='MyVisitedPlace'),
    path('myvisitedmeeting/',MaeumCheck.views.MyVisitedMeeting,name='MyVisitedMeeting'),
    path('placeqrcodeimg/<int:code_id>',MaeumCheck.views.PlacegenQR,name="PlaceQRCodeImg"),
    path('placeqrcodeimg/exit/<int:code_id>/img/',MaeumCheck.views.PlaceExitgenQR,name="PlaceExitQRCodeImg"),
    path('meetingqrcodeimg/<int:code_id>',MaeumCheck.views.MeetinggenQR,name="MeetingQRCodeImg"),
    path('placeqrshow/<int:code_id>/comments/',MaeumCheck.views.PlaceSaveComplete,name="PlaceSaveComplete"),
    path('meetingqrshow/<int:code_id>/comments/',MaeumCheck.views.MeetingSaveComplete,name="MeetingSaveComplete"),    
    path('accounts/', include('allauth.urls')),
    path('myplacelist/',MaeumCheck.views.MyPlaceList,name='MyPlaceList'),
    path('mymeetinglist/',MaeumCheck.views.MyMeetingList,name='MyMeetingList'),
    path('placeqrshow/<int:code_id>/exit/', MaeumCheck.views.Getout, name="Getout"),
    path('deleteplace/<int:id>',MaeumCheck.views.DeletePlace, name="DeletePlace"),
    path('deletemeeting/<int:id>',MaeumCheck.views.DeleteMeeting, name="DeleteMeeting"),
]
