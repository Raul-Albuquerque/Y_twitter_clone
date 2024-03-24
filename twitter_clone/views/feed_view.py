from django.shortcuts import render, redirect

def feed(request):
  return render(request, 'feed_profile.html')