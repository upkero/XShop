from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.validators import FileExtensionValidator
# from django.core.exceptions import ValidationError
# from PIL import Image

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

class ChangeAvatarForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = (
            "image",
        )
    
    image = forms.ImageField(
        required=False,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])
        ],
        )
    
    # def clean_image(self):
    #     image = self.cleaned_data.get('image')

    #     if image:
    #         if image.size > 2 * 1024 * 1024:
    #             raise forms.ValidationError("Image file too large ( > 2MB )")
            
    #         try:
    #             img = Image.open(image)
    #             img.verify()
    #         except Exception:
    #             raise forms.ValidationError("Invalid image file")
        
    #     return image

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
    
class UserPasswordChangeForm(PasswordChangeForm):
    pass