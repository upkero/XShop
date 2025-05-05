from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart-add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart-change/<int:product_id>/', views.cart_change, name='cart_change'),
    path('cart-remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]