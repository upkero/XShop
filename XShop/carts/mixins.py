from django.template.loader import render_to_string
from carts.models import Cart
from carts.utils import get_user_carts


class CartMixin:
    def get_cart(self, request, product=None, cart_id=None):
        if request.user.is_authenticated:
            query_kwargs = {'user': request.user}
        else:
            query_kwargs = {'session_key': request.session.session_key}
        
        if product:
            query_kwargs['product'] = product
        
        if cart_id:
            query_kwargs['id'] = cart_id
        
        return Cart.objects.filter(**query_kwargs).first()
    
    def render_cart(self, request):
        return render_to_string(
            'carts/includes/included_cart.html', 
            {'carts': get_user_carts(request)}, 
            request=request
        )