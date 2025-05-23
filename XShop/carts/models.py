from django.db import models

from goods.models import Products
from users.models import User


class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.product_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='User')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Item')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Quantity')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Date added')
    
    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        ordering = ('id',)
        
    objects = CartQueryset().as_manager()
        
    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
        
    def __str__(self):
        cart_name = self.user.username if self.user else str(self.session_key)[:8]
        return f'Cart {cart_name} | Item {self.product.name} | Quantity {self.quantity}'
