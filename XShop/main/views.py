from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def index(request):
    context = {
        'products':[
            {'image': 'img/goods/1.png', 'name': 'Green Tea', 'strength': 2, 'price': 15.00},
            {'image': 'img/goods/2.png', 'name': 'Black Tea', 'strength': 9, 'price': 10.00},
            {'image': 'img/goods/3.png', 'name': 'White Tea', 'strength': 5, 'price': 20.00},
            {'image': 'img/goods/4.png', 'name': 'Jasmine Tea', 'strength': 6, 'price': 56.00},
        ]
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

