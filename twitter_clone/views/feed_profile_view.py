from django.shortcuts import render, redirect

def feed_profile(request):
  return render(request, 'feed_profile.html')