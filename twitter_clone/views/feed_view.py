from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from ..models import Profile

# Feed view

def feed(request):

  # check if user is authenticated
  if request.user.is_authenticated:
    user = User.objects.get(id=request.user.id)

    # Find the user profile from his ID
    profile = Profile.objects.get(user_id=request.user.id)

    # render the feed page for the user
    return render(request, "feed.html", {"profile": profile})

  # User will be redirect to create account or login
  return redirect("home")


# Follow view

def follow(request, pk):
  # check if user is authenticated
  if request.user.is_authenticated:

    # select the user to follow from his id
    profile = Profile.objects.get(user_id=pk)

    # add the user to follow in the db follows
    request.user.profile.follows.add(profile)

    # save the previous action
    request.user.profile.save()

    # then the user will be redirect to the page he was before he follows the other User
    return redirect(request.META.get("HTTP_REFERER"))

  # If the user isn´t authenticated he will be redirect to create account or login
  return redirect("home")

def unfollow(request, pk):
  # check if user is authenticated
  if request.user.is_authenticated:

    # select the user to follow from his id
    profile = Profile.objects.get(user_id=pk)

    # remove the relationship between the users
    request.user.profile.remove(profile)

    # save the previous action
    request.user.profile.save()

    # then the user will be redirect to the page he was before he unfollows the other User
    return redirect(request.META.get("HTTP_REFERER"))
  
  # If the user isn´t authenticated he will be redirect to create account or login
  return redirect("home")