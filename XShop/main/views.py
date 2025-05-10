from django.shortcuts import render

from goods.models import Products
import random


def index(request):

    products = list(Products.objects.filter(is_active=True, category__is_active=True))
    random.shuffle(products)
    recommended_products = products[:4]
    
    context = {
        'recommended_products': recommended_products,
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def delivery(request):
    return render(request, 'main/delivery.html')


def policy(request):
    return render(request, 'main/policy.html')


def terms(request):
    return render(request, 'main/terms.html')


def ordandret(request):
    return render(request, 'main/ordandret.html')

