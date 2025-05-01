from tabnanny import verbose
from unicodedata import category
from django.db import models


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
        ordering = ['id',]
        
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
    is_new = models.BooleanField(
        default=True
    )
    
    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
    def __str__(self):
        return f'{self.name} / Quantity - {self.quantity}'
    
    def display_id(self):
        return f'{self.id:05}'
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price