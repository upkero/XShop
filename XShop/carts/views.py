from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View

from carts.mixins import CartMixin
from carts.utils import get_user_carts
from goods.models import Products
from carts.models import Cart


class CartAddView(CartMixin, View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        product = Products.objects.get(id=product_id)

        cart = self.get_cart(request, product=product)

        if cart:
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(
                user=request.user if request.user.is_authenticated else None,
                session_key=request.session.session_key if not request.user.is_authenticated else None,
                product=product,
                quantity=1,
            )
            
        response_data = {
            "message": "Product added to cart",
            "cart_items_html": self.render_cart(request),
        }

        return JsonResponse(response_data)


class CartChangeView(CartMixin, View):
     def post(self, request):
        cart_id = request.POST.get("cart_id")
        cart = self.get_cart(request, cart_id=cart_id)
        cart.quantity = int(request.POST.get("quantity"))
        cart.save()

        quantity = cart.quantity
        
        response_data = {
            "message": "Item quantity updated",
            "quantity": quantity,
            "cart_items_html": self.render_cart(request),
        }

        return JsonResponse(response_data)


def cart_remove(request):
    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)

    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request
    )

    response_data = {
        "message": "Product removed from cart",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)
