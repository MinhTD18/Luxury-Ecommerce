from django.contrib.auth.views import *
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
            return redirect('shipping_address')
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


def logout(request):
    auth.logout(request)
    return redirect('main')


def shipping_address(request):
    return render(request, 'store/08_Shipping_Address.html')


def payment(request):
    return render(request, 'store/09_payment.html')


def summary(request):
    return render(request, 'store/10_summary.html')


def finish(request):
    return render(request, 'store/11_finish.html')


def product(request):
    return render(request, 'store/03_product.html')


def handle404(request):
    return render(request, 'store/404.html')


def contact(request):
    return render(request, 'store/14_contact.html')


def blog(request):
    return render(request, 'store/12_blog.html')


def single_blog_post(request):
    return render(request, 'store/13_single-blog-post.html')


def short_code(request):
    return render(request, 'store/shortcodes.html')


def about(request):
    return render(request, 'store/about.html')


def look_book(request):
    return render(request, 'store/look-book.html')


def categories(request):
    return render(request, 'store/02_categories.html')


def shopping_cart(request):
    return render(request, 'store/06_shopping_cart.html')


def single_product_1(request):
    return render(request, 'store/04_single_product.html')


def single_product_2(request):
    return render(request, 'store/04_single_product-2.html')


class CustomPasswordResetView(PasswordResetView):
    subject_template_name = 'store/registration/password_reset_subject.txt'
    email_template_name = 'store/registration/password_reset_email.html'
    template_name = 'store/registration/password_reset_form.html'


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
