from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from ..models import Tweet

def like_tweet(request, pk):
  # check if user is authenticated
  if request.user.is_authenticated:

    # find the tweet from his id
    tweet = get_object_or_404(Tweet, id=pk)

    if tweet.likes.filter(id=request.user.id):
      tweet.likes.remove(request.user)
    else:
      tweet.likes.add(request.user)

    return redirect(request.META.get("HTTP_REFERER"))
  
  return redirect("home")

