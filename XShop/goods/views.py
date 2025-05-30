from django.core.paginator import Paginator
from django.db.models import F, Avg, DecimalField, ExpressionWrapper
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from goods.models import Categories, Products
from goods.utils import q_search
from orders.models import OrderItem
from reviews.forms import ReviewForm
from reviews.models import Review


class CatalogView(ListView):
    queryset = Products.objects.filter(is_active=True, category__is_active=True)
    template_name = 'goods/catalog.html'
    context_object_name = 'products'
    paginate_by = 12
    allow_empty = False

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        query = self.request.GET.get('q')
        order_by = self.request.GET.get('order_by', 'default')
        on_sale = self.request.GET.get('on_sale')
        new = self.request.GET.get('new')
        # favorites = self.request.GET.get('favorites')

        if query:
            products = q_search(query)
        elif not category_slug:
            products = self.queryset
        else:
            products = self.queryset.filter(category__slug=category_slug)
            if not products.exists():
                raise Http404()

        if order_by in ("sell_price", "-sell_price"):
            products = products.annotate(
                sell_price=ExpressionWrapper(
                    F("price") - (F("price") * F("discount") / 100),
                    output_field=DecimalField()
                )
            ).order_by(order_by)
        elif order_by != "default":
            products = products.order_by(order_by)
        if on_sale:
            products = products.filter(discount__gt=0)
        if new:
            products = products.filter(is_new=True)
        # if favorites:
        #     products = products.filter()

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        page = self.request.GET.get('page', 1)
        paginator = context['paginator']
        total_pages = paginator.num_pages
        
        try:
            current_page = int(page)
        except (TypeError, ValueError):
            current_page = 1
        
        start = max(1, current_page - 1)
        end = min(total_pages, current_page + 1)
        if (end - start) < 2:
            if start == 1:
                end = min(total_pages, start + 2)
            elif end == total_pages:
                start = max(1, end - 2)
                
        context['page_range_start'] = start
        context['page_range_end'] = end
        context['slug_url'] = self.kwargs.get('category_slug')
        
        if self.kwargs.get('category_slug'):
            context['category'] = Categories.objects.get(slug=self.kwargs['category_slug'])

        return context


class ProductView(DetailView):

    template_name = "goods/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=...):
        return get_object_or_404(
            Products,
            slug=self.kwargs.get(self.slug_url_kwarg),
            is_active=True,
            category__is_active=True,
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = context["product"]
        user = self.request.user
        
        user_review = None
        if user.is_authenticated:
            user_review = Review.objects.filter(user=user, product=product).first()

        can_review = (
            user.is_authenticated
            and OrderItem.objects.filter(order__user=user, order__status='Completed', product=product).exists()
            and not user_review
        )

        reviews = Review.objects.select_related('user').filter(product = product)
        if user.is_authenticated:
            reviews = reviews.exclude(user=user)
        
        
        average_rating = (
            product.reviews.aggregate(avg=Avg("rating"))["avg"] or 0
        )
        context["average_rating"] = round(average_rating, 1)
        
        context["review_form"] = ReviewForm()
        context["can_review"] = can_review
        context["user_review"] = user_review
        context["reviews"] = reviews
        context["product"] = product

        return context