from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db.models import Count
from django.contrib.auth.models import User

from ..models import Profile
from ..forms import EditProfileForm

def feed_profile(request):
  if request.user.is_authenticated:
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)
    profiles = Profile.objects.exclude(user=request.user)

    following = Profile.objects.get(user_id=request.user.id).follows.count() - 1
    followers = Profile.objects.get(user_id=request.user.id).followed_by.count() - 1

    if request.method == "POST":
      profile_form = EditProfileForm(request.POST or None, request.FILES or None, instance=profile)
      if profile_form.is_valid():
        profile_form.save()
        profile_form = EditProfileForm()
        login(request, user)
        return redirect("profile")
      
    profile_form = EditProfileForm()
    return render(request, "feed_profile.html", {"form": profile_form, "profile": profile, "following": following, "followers": followers, "profiles": profiles})
  
  else:
    return redirect("home")