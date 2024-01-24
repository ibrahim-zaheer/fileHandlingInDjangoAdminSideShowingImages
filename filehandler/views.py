from django.shortcuts import render
from django.http import HttpResponse
from .models import ProfileData
# Create your views here.

#use this view function to get the models and then accessing their data

def hello(request):
    profile_queryset = ProfileData.objects.all()
    return render(request,"home.html",{"profile_queryset":profile_queryset})
