from django.shortcuts import render


def base(request):
    return render(request, "base.html")


def home(request):
    if request.user.is_authenticated:
        return render(
            request,
            "feed_tweets.html",
        )

    return render(request, "home.html")
