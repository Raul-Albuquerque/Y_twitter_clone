from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse

from django.contrib.auth.models import User


from ..forms import TweetForm
from ..models import Tweet, Profile

def feed_tweets(request):
  if request.user.is_authenticated:
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)
    form = TweetForm(request.POST or None, request.FILES or None)
    profiles = Profile.objects.exclude(user=request.user)
    following = Profile.objects.get(user_id=request.user.id)

    if request.method == "POST":
      if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        form = TweetForm()
        return redirect("feed_tweets")
      else:
        form = TweetForm()
    tweets = Tweet.objects.all().order_by("-tweet_date")
    return render(request, 'feed_tweets.html', {"tweets": tweets, "form": form, "profile": profile, "profiles": profiles, "user": user, "following": following})
  else:
    return redirect("home")