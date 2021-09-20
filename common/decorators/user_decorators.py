from django.shortcuts import redirect
from django.urls import reverse

from functools import wraps


def login_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not hasattr(request, 'session') or 'shop' not in request.session:
            if not request.user.is_authenticated:
                request.session['return_to'] = request.get_full_path()
                return redirect(reverse('login'))
        return func(request, *args, **kwargs)

    return wrapper