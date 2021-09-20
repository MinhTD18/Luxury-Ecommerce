from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('product/', views.product, name='product'),
    path('single_product_1/', views.single_product_1, name='single_product_1'),
    path('single_product_2/', views.single_product_2, name='single_product_2'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('404/', views.handle404, name='404'),
    path('contact/', views.contact, name='contact'),
    path('single_blog_post/', views.single_blog_post, name='single_blog_post'),
    path('blog/', views.blog, name='blog'),
    path('short_code/', views.short_code, name='short_code'),
    path('about/', views.about, name='about'),
    path('look_book/', views.look_book, name='look_book'),
    path('categories/', views.categories, name='categories'),
]