from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:home')
        else:
            messages.info(request, 'Usuario o contraseña incorrecto')
    return render(request, 'Users/login.html')


@login_required(redirect_field_name='login')
def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('users:login')
