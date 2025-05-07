from django.contrib import admin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabularAdmin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'username', 'email']
    
    inlines = [CartTabAdmin, OrderTabularAdmin]
    
    fields = [
        'username', 
        'image',
        ('first_name', 'last_name'),
        'email',
        'password',
        ('last_login', 'date_joined'),
        ('is_superuser', 'is_staff'),
        'user_permissions',
        'groups',
        
        'is_active',
    ]