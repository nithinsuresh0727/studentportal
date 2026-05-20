from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    return render(request, "login.html")

def register_view(request):
    return render(request, "register.html")

def dashboard_view(request):
    return render(request, "dashboard.html")

def logout_view(request):
    logout(request)
    return redirect('login')