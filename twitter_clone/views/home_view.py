from django.shortcuts import render, redirect


def base(request):
    return render(request, "base.html")


def home(request):
    if request.user.is_authenticated:
        return redirect("feed_tweets")

    return render(request, "home.html")
