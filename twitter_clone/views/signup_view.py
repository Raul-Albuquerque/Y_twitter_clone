from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from ..forms import SignUpForm


from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["usuario"]
            first_name = form.cleaned_data["nome"].lower()
            last_name = form.cleaned_data["sobrenome"].lower()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["senha"]

            double_user = User.objects.filter(username=username).first()

            if double_user:
                return HttpResponse("The username already exists.")
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                )
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect("feed_tweets")
        else:
            return HttpResponse("Something went wrong. Try again later.")
    else:
        form = SignUpForm()
        return render(request, "signup.html", {"form": form})
