from django.db import models

from users.models import User
from goods.models import Products


class ReviewModel(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Product')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Rating')
    comment = models.TextField(verbose_name='Comment')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    
    class Meta:
        db_table = 'review'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ('-created_at',)
        unique_together = ('user', 'product')
        
    def __str__(self):
        return f"{self.user.username} on {self.product.name} ({self.rating}★)"
    