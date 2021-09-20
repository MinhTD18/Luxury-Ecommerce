from django.contrib.auth.views import *
from django.shortcuts import render, redirect


def main(request):
    context = {}
    return render(request, 'store/index.html', context)


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
