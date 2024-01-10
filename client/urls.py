from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="client_index"),
    path("profile", views.profile, name="client_profile"),
    path("login", views.login, name="client_login"),
    path("logout", views.logout, name="client_logout"),
    path("signup", views.signup, name="client_signup")
]