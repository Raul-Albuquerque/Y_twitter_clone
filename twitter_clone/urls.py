from .views import home_view, signup_view, signin_view
from django.urls import path

urlpatterns = [
    path("", home_view.home, name="home"),
    path("signup/", signup_view.signup, name="signup"),
    path("signin/", signin_view.signin, name="signin"),
]
