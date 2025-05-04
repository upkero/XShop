from email.mime import image
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )

    username = forms.CharField()
    password = forms.CharField()

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

class ChangeAvatarForm:
    
    class Meta:
        model = User
        fields = (
            "image",
        )
    
    image = forms.ImageField()

class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )
    
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()