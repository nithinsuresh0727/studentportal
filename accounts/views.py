from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from django.http import HttpResponse
import csv


def register_view(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'accounts/login.html')


@login_required
def dashboard_view(request):

    form = StudentForm()

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            student_name = form.cleaned_data['student_name']

            response = HttpResponse(content_type='text/csv')

            response['Content-Disposition'] = 'attachment; filename="student.csv"'

            writer = csv.writer(response)

            writer.writerow(['Student Name', 'User Email'])

            writer.writerow([
                student_name,
                request.user.email
            ])

            return response

    return render(
        request,
        'accounts/dashboard.html',
        {'form': form}
    )


def logout_view(request):
    logout(request)
    return redirect('login')