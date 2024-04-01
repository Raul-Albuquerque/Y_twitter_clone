from django.shortcuts import redirect

from ..models import Profile


def unfollow(request, pk):
    if request.user.is_authenticated:

        profile = Profile.objects.get(user_id=pk)

        request.user.profile.follows.remove(profile)

        request.user.profile.save()

        return redirect(request.META.get("HTTP_REFERER"))

    return redirect("home")
