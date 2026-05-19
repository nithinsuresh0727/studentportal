from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

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

            else:
                return render(request, 'accounts/login.html', {
                    'error': 'Invalid Password'
                })

        except User.DoesNotExist:

            return render(request, 'accounts/login.html', {
                'error': 'Invalid Username or Email'
            })

    return render(request, 'accounts/login.html')