from django.shortcuts import render, redirect

def feed(request):
  return render(request, 'feed.html')