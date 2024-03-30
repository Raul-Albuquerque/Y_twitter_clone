from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from ..forms import SignUpForm


def base(request):
    return render(request, "base.html")


def home(request):
    if request.user.is_authenticated:
        return redirect("feed_tweets")

    return render(request, "home.html")
