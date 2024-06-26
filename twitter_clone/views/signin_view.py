from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from ..forms import SignInForm


def signin(request):
    form = SignInForm()
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["usuario"].lower()
            password = form.cleaned_data["senha"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("feed_tweets")

        return HttpResponse("Check out your informations.")

    return render(request, "signin.html", {"form": form})
