from .views import home_view, signup_view
from django.urls import path

urlpatterns = [
    path("", home_view.home, name="home"),
    path("signup/", signup_view.signup, name="signup"),
    path("signin/", home_view.signin, name="signin"),
]
