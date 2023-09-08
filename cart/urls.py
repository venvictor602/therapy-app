from django.urls import path

from . import views

urlpatterns = [
    path('checkup/', views.checkup,name='checkup'),
    path('cart/checkup/<str:ref>/', views.verify_payment, name='verify-payment'),

    path('cart/', views.cart_detail, name='cart'),
    path('success/', views.success, name='success'),


]