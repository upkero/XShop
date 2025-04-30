from django.shortcuts import render
from django.template import context

from goods.models import Products


def catalog(request):
    products = Products.objects.filter(is_active=True)
    
    context = {
        'products': products,
    }
    
    return render(request, 'goods/catalog.html', context)


def product(request, product_id):
    product = Products.objects.filter(id=product_id, is_active=True).first()
    
    context = {
        'product' : product,
    }
    
    return render(request, 'goods/product.html', context)