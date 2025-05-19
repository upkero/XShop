from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    
    path('change-password/', views.UserPasswordChangeView.as_view(), name='changepass'),
    path('edit-profile/', views.UserEditProfileView.as_view(), name='editprofile'),
    path('forgot-password/', views.UserForgotPasswordView.as_view(), name='forgotpass'),
    path('delete/', views.UserDeleteAccountView.as_view(), name='delete_account'),
    
    path('cart/', views.UserCartView.as_view(), name='users_cart'),
]