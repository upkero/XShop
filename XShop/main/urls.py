from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('delivery/', views.delivery, name='delivery'),
    path('policy/', views.policy, name='policy'),
    path('terms/', views.terms, name='terms'),
    path('order-and-return/', views.ordandret, name='order_and_return'),
]