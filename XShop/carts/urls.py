from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('add/<slug:product_slug>/', views.cart_add, name='add'),
    path('change/<slug:product_slug>/', views.cart_change, name='change'),
    path('remove/<slug:product_slug>/', views.cart_remove, name='remove'),
]