from django.urls import path

from reviews import views


app_name = 'reviews'

urlpatterns = [
    path('create/', views.ReviewCreateView.as_view(), name='create'),
    path('edit/', views.ReviewEditView.as_view(), name='edit'),
    path('delete/', views.ReviewDeleteView.as_view(), name='delete'),
]