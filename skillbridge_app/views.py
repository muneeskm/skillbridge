from urllib import request

from django.shortcuts import render
from django import views
from django.contrib import admin
from django.urls import path
from skillbridge_app import views

# Create your views here.
def home(request):
	return render(request, 'home.html')

def jobs(request):
    return render(request, 'jobs.html')

def login(request):
    return render(request, 'login.html')

def post(request):
    return render(request, 'post.html')

def signup(request):
    return render(request, 'signup.html')


urlpatterns = [
    path('',views.home,name="home"),
    path('/jobs', views.jobs, name="jobs"),
    path('/login', views.login, name="login"),
    path('/post', views.post, name="post"),
    path('/signup', views.signup, name="signup")
]

from skillbridge_app.models import occupation
def occupation(request):
    all_occ = occupation.objects.all()
    context = {
        'occupations': all_occ,
        'page_title': 'OCCUPATION DETAILS'
    }
    return render(request, 'occupation.html', context)
