from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('add/', views.CartAddView.as_view(), name='add'),
    path('change/', views.CartChangeView.as_view(), name='change'),
    path('remove/', views.cart_remove, name='remove'),
]