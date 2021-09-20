from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('shipping_address/', views.shipping_address, name='shipping_address'),
    path('payment/', views.payment, name='payment'),
    path('summary/', views.summary, name='summary'),
    path('finish/', views.finish, name='finish'),
]