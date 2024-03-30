from django.shortcuts import redirect, get_object_or_404

from ..models import Tweet


def delete_tweet(request, pk):
    if request.user.is_authenticated:
        tweet = get_object_or_404(Tweet, id=pk)

        if request.user.username == tweet.user.username:
            tweet.delete()

            return redirect(request.META.get("HTTP_REFERER"))

    return redirect("home")
