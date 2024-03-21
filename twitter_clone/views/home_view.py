from django.shortcuts import render
from django.http import HttpResponse

def base(request):
  return render(request, 'base.html')

def home(request):
  return render(request, 'home.html')

def signup(request):
  return render(request, 'signup.html')

def signin(request):
  return render(request, 'signin.html')