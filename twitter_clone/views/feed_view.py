from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from ..models import Profile


# feed_view
def feed(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user_id=request.user.id)
        profiles = Profile.objects.exclude(user=request.user)

        following = Profile.objects.get(user_id=request.user.id)

        return render(
            request,
            "feed.html",
            {
                "profile": profile,
                "profiles": profiles,
                "following": following,
                "user": user,
            },
        )

    return redirect("home")
