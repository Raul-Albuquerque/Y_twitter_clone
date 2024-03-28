from django.shortcuts import redirect, get_object_or_404

from ..models import Tweet

def like_tweet(request, pk):
  if request.user.is_authenticated:
    tweet = get_object_or_404(Tweet, id=pk)

    if tweet.likes.filter(id=request.user.id):
      tweet.likes.remove(request.user)
    else:
      tweet.likes.add(request.user)

    return redirect(request.META.get("HTTP_REFERER"))
  
  return redirect("home")

