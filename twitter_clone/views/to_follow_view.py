from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from ..models import Profile

# feed_view

def to_follow(request):
  if request.user.is_authenticated:
    profile = Profile.objects.get(user_id=request.user.id)
    profiles = Profile.objects.exclude(user=request.user)

    return render(request, "to_follow.html", {"profile": profile, "profiles": profiles})

  return redirect("home")