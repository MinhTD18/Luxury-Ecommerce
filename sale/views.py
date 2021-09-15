from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, \
    PasswordChangeView, PasswordChangeDoneView
from django.views.generic.base import View

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def main(request):
    context = {}
    return render(request, 'store/index.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Email or Password is not correct')
            return redirect('login')
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


class CustomPasswordResetViewDone(PasswordResetDoneView):
    template_name = 'store/registration/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'store/registration/password_reset_confirm.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'store/registration/password_reset_complete.html'


class CustomPasswordChangeView(PasswordChangeView):
    # template_name = 'store/registration/password_change_form.html'
    pass


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    # template_name = 'store/registration/password_change_done.html'
    pass