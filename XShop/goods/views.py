from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from goods.models import Categories, Products


def catalog(request, category_slug=False):
    
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    new = request.GET.get('new', None)
    # favorites = request.GET.get('favorites', None)
    
    if category_slug:
        products = get_list_or_404(Products.objects.filter(is_active=True, category__slug=category_slug))
    else:
        products = Products.objects.filter(is_active=True)
    
    if on_sale:
        products = products.filter(discount__gt=0)
    if new:
        products = products.filter(is_new=True)
    # if favorites:
    #     products = products.filter()
    
    paginator = Paginator(products, 4)
    current_page = paginator.page(int(page))
    
    context = {
        'products': current_page,
        'slug_url': category_slug,
    }
    
    if category_slug:
        context['category'] = Categories.objects.get(slug = category_slug)
    
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.filter(slug=product_slug, is_active=True).first()
    
    context = {
        'product' : product,
    }
    
    return render(request, 'goods/product.html', context)