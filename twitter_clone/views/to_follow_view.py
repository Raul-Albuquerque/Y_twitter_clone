from django.shortcuts import render, redirect

from ..models import Profile


def to_follow(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=request.user.id)
        profiles = Profile.objects.exclude(user=request.user)

        return render(
            request, "to_follow.html", {"profile": profile, "profiles": profiles}
        )

    return redirect("home")
