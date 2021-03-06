from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .views import *

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('shipping_address/', views.shipping_address, name='shipping_address'),
    path('payment/', views.payment, name='payment'),
    path('summary/', views.summary, name='summary'),
    path('finish/', views.finish, name='finish'),
    path('product/', views.product, name='product'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetViewDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
]