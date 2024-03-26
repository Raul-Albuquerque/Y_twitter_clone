from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse


from ..forms import TweetForm
from ..models import Tweet

def feed_tweets(request):
  if request.user.is_authenticated:
    form = TweetForm(request.POST or None)
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
    return render(request, 'feed_tweets.html', {"tweets": tweets, "form": form})
  else:
    return redirect("home")