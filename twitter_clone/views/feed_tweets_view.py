from django.shortcuts import render, redirect

def feed_tweets(request):
  return render(request, 'feed_tweets.html')