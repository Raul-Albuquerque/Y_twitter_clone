from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse

from ..models import Profile


def follow(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)

        request.user.profile.follows.add(profile)

        request.user.profile.save()

        return redirect(request.META.get("HTTP_REFERER"))

    return redirect("home")
