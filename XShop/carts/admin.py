from django.contrib import admin

from carts.models import Cart


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'quantity', 'created_timestamp'
    search_fields = 'product', 'quantity', 'created_timestamp'
    readonly_fields = ('created_timestamp',)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_dysplay', 'product_dysplay', 'quantity', 'created_timestamp']
    list_filter = ['created_timestamp', 'user', 'product__name']
    search_fields = ['user', 'product__name']
    
    def user_dysplay(self, obj):
        if obj.user:
            return str(obj.user)
        return "Anonymous user"
    
    def product_dysplay(self, obj):
        return str(obj.product.name)