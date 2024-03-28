from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
  if request.user.is_authenticated:
    logout(request)
    
  return redirect("home")