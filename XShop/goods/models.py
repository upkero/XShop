from tabnanny import verbose
from unicodedata import category
from django.db import models

from decimal import Decimal


class Categories(models.Model):
    name = models.CharField(
        max_length=150, 
        unique=True, 
        verbose_name="Name"
    )
    slug = models.SlugField(
        max_length=200, 
        unique=True,
        blank=True, 
        null=True, 
        verbose_name="URL"
    )
    is_active = models.BooleanField(
        default=True
    )
    
    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name
        

class Products(models.Model):
    STRENGTH_CHOICES = [(i, str(i)) for i in range(0, 11)]
    
    name = models.CharField(
        max_length=150, 
        unique=True, 
        verbose_name="Name"
    )
    slug = models.SlugField(
        max_length=200, 
        unique=True, 
        blank=True, 
        null=True, 
        verbose_name="URL"
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Description"
    )
    image = models.ImageField(
        upload_to='goods_images', 
        blank=True, null=True, 
        verbose_name="Image"
    )
    strength = models.PositiveSmallIntegerField(
        verbose_name="Strength",
        choices=STRENGTH_CHOICES,
        default=0,
    )
    price = models.DecimalField(
        default=0.00, 
        max_digits=5, 
        decimal_places=2, 
        verbose_name="Price"
    )
    discount = models.DecimalField(
        default=0.00, 
        max_digits=4, 
        decimal_places=2, 
        verbose_name="Discont %"
    )
    quantity = models.PositiveIntegerField(
        default=0, 
        verbose_name="Quantity"
    )
    category = models.ForeignKey(
        to=Categories, 
        on_delete=models.CASCADE, 
        verbose_name="Category"
    )
    is_active = models.BooleanField(
        default=True
    )
    
    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
    def __str__(self):
        return f'{self.name} / Quantity - {self.quantity}'
    
    def get_discounted_price(self):
        if self.discount:
            discounted_price = self.price * (Decimal('1.00') - self.discount)
            return round(discounted_price, 2)
        return self.price