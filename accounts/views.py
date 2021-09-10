from django.contrib.auth.forms import UsernameField
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
        if request.method == "POST":
            form= RegistrationForm( request.POST or None)
            if form.is_valid():
                user = form.save()
                raw_password = form.cleaned_data.get('password1')
                #Authenticate the user
                user= authenticate(username= user.username, password= raw_password )
                login= (request, user)
                return redirect("main:home")
        else:
                form= RegistrationForm()
        return render(request, "accounts/register.html", {"form":form}) 
def login_user(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
        if request.method == "POST":
            username= request.POST['username']
            password= request.POST['password']
            user= authenticate(username= username, password= password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("main:home")
                else:
                    return render(request, 'accounts/login.html',{"error": "Your account has been disabled."})
            else:
                return render(request, 'accounts/login.html',{"error": " Invalid username or passowrd Try again"})
        return render(request,'accounts/login.html' )
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        print("logout successfully")
        return redirect("accounts:login")
    else:
        return redirect("accounts:login")


