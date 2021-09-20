from django.contrib.auth.views import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from common.decorators.user_decorators import login_required


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('shipping_address')
        else:
            messages.info(request, 'Email or Password is not correct')
            return redirect('login')

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('main')
        else:
            return render(request, 'store/07_login_register.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User name is taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password is not matching!')
            return redirect('register')
        return redirect('/')

    return render(request, 'store/05_register.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('main')


@login_required
def shipping_address(request):
    return render(request, 'store/08_Shipping_Address.html')


@login_required
def payment(request):
    return render(request, 'store/09_payment.html')


@login_required
def summary(request):
    return render(request, 'store/10_summary.html')


@login_required
def finish(request):
    return render(request, 'store/11_finish.html')
