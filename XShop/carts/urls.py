from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('add/', views.CartAddView.as_view(), name='add'),
    path('change/', views.cart_change, name='change'),
    path('remove/', views.cart_remove, name='remove'),
]