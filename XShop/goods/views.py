from django.shortcuts import render, get_object_or_404

from goods.models import Products


def catalog(request, category_slug=False):
    if category_slug:
        products = get_object_or_404(Products.objects.filter(is_active=True, category__slug=category_slug))
    else:
        products = Products.objects.filter(is_active=True)
    
    context = {
        'products': products,
    }
    
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.filter(slug=product_slug, is_active=True).first()
    
    context = {
        'product' : product,
    }
    
    return render(request, 'goods/product.html', context)