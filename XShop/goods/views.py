from django.shortcuts import render
from django.template import context


def catalog(request):
    context = {
        'products': [
            {'image': 'img/goods/1.png', 'name': 'Green Tea', 'strength': 8, 'price': 15.00},
            {'image': 'img/goods/2.png', 'name': 'Black Tea', 'strength': 1, 'price': 10.00},
            {'image': 'img/goods/3.png', 'name': 'White Tea', 'strength': 4, 'price': 20.00},
            {'image': 'img/goods/4.png', 'name': 'Jasmine Tea', 'strength': 9, 'price': 18.00},
            {'image': 'img/goods/5.png', 'name': 'Lemon Tea', 'strength': 10, 'price': 12.00},
            {'image': 'img/goods/6.png', 'name': 'Mint Tea', 'strength': 7, 'price': 14.00},
            {'image': 'img/goods/7.png', 'name': 'Bergamot Tea', 'strength': 6, 'price': 16.00},
            {'image': 'img/goods/8.png', 'name': 'Pu-erh Tea', 'strength': 6, 'price': 22.00},
            {'image': 'img/goods/9.png', 'name': 'Weight Loss Tea', 'strength': 5, 'price': 25.00},
            {'image': 'img/goods/1.png', 'name': 'Rooibos',  'strength': 3, 'price': 19.00},
            {'image': 'img/goods/2.png', 'name': 'Hibiscus Tea', 'strength': 9, 'price': 17.00},
            {'image': 'img/goods/3.png', 'name': 'Honey Tea', 'strength': 8, 'price': 21.00},
            {'image': 'img/goods/4.png', 'name': 'Ginger Tea', 'strength': 7, 'price': 16.00},
            {'image': 'img/goods/5.png', 'name': 'Raspberry Tea', 'strength': 10, 'price': 15.50},
            {'image': 'img/goods/6.png', 'name': 'Orange Tea', 'strength': 2, 'price': 18.50},
            {'image': 'img/goods/7.png', 'name': 'Cinnamon Tea', 'strength': 7, 'price': 14.00}
        ]
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    context = {
        'product': {
            'id': 123,
            'image': 'img/goods/5.png', 
            'name': 'Lemon Tea', 
            'strength': 10, 
            'price': 12.00,
            'description': 'This tea is a delicate blend of forest herbs, delivering calmness and aroma in every cup. Ideal for afternoon relaxation and meditation moments.'
        }
    }
    return render(request, 'goods/product.html', context)