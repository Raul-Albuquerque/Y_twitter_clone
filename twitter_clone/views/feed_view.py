from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from ..models import Profile

# feed_view

def feed(request):
  if request.user.is_authenticated:
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)
    profiles = Profile.objects.exclude(user=request.user)

    user_follows = user.profile.follows.filter(id=profile.id).exists()

    return render(request, "feed.html", {"profile": profile, "profiles": profiles, "follows": user_follows})

  return redirect("home")