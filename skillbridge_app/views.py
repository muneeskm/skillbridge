from urllib import request

from django.shortcuts import render
from django import views
from django.contrib import admin
from django.urls import path
from skillbridge_app import views

# Create your views here.
def home(request):
	return render(request, 'home.html')


urlpatterns = [
    path('',views.home,name="home")
]

from skillbridge_app.models import occupation
def occupation(request):
    all_occ = occupation.objects.all()
    context = {
        'occupations': all_occ,
        'page_title': 'OCCUPATION DETAILS'
    }
    return render(request, 'occupation.html', context)
