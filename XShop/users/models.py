from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(
        _("email address"), 
        unique=True,
        blank=True,
        error_messages={
            "unique": _("This email is already in use."),
        },
    )
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name="Profile picture")
    
    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"
        
    def __str__(self):
        return self.username