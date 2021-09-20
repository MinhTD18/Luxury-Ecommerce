from django.urls import path, include

urlpatterns = [
    path('', include('sale.shops.urls'), name='shops'),
    path('users/', include('sale.users.urls'), name='users'),
]
