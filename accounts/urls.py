from django.urls import path
from main import views
from .import views
from django.http import HttpResponse
app_name = "accounts"
urlpatterns = [
    path("register/", views.register, name= "register"),
    path("login/", views.login_user, name= "login"),
    path("logout/", views.logout_user, name= "logout"),
]