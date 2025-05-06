from django.contrib import admin

from goods.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',) }
    list_display = ['name', 'is_active']
    list_editable = ['is_active']
    
    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',) }
    list_display = ['name', 'quantity', 'price', 'discount', 'is_new', 'is_active']
    list_editable = ['discount', 'is_new', 'is_active']
    search_fields = ['name', 'description']
    list_filter = ['discount', 'quantity', 'category']
    fields = [
        'name',
        ('is_active', 'is_new'),
        'category',
        'slug',
        'strength',
        'description',
        'image',
        ('price', 'discount'),
        'quantity'
    ]