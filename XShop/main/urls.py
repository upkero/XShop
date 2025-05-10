from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('delivery/', views.DeliveryView.as_view(), name='delivery'),
    path('policy/', views.PolicyView.as_view(), name='policy'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('order-and-return/', views.OrdandretView.as_view(), name='order_and_return'),
]