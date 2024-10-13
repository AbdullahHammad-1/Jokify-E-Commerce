from tkinter.font import names

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:id>/', views.detail, name='detail'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]