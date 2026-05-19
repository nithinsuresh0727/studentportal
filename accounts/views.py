from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import csv


# REGISTER
def register_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'accounts/register.html')


# LOGIN
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:

            user_obj = User.objects.get(
                username=username,
                email=email
            )

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                return redirect('dashboard')

        except User.DoesNotExist:
            pass

    return render(request, 'accounts/login.html')


# DASHBOARD
def dashboard_view(request):

    if request.method == 'POST':

        student_name = request.POST.get('student_name')

        response = HttpResponse(content_type='text/csv')

        response['Content-Disposition'] = 'attachment; filename="student.csv"'

        writer = csv.writer(response)

        writer.writerow(['Student Name', 'User Email'])

        writer.writerow([
            student_name,
            request.user.email
        ])

        return response

    return render(request, 'accounts/dashboard.html')


# LOGOUT
def logout_view(request):

    logout(request)

    return redirect('login')