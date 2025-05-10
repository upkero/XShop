from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from goods.models import Categories, Products
from goods.utils import q_search


def catalog(request, category_slug=False):

    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        page = 1

    query = request.GET.get("q", None)

    order_by = request.GET.get("order_by", "default")

    on_sale = request.GET.get("on_sale", None)
    new = request.GET.get("new", None)
    # favorites = request.GET.get('favorites', None)

    if query:
        products = q_search(query)
    elif not category_slug:
        products = Products.objects.filter(is_active=True, category__is_active=True)
    else:
        products = Products.objects.filter(
            is_active=True, category__is_active=True, category__slug=category_slug
        )
        if not products.exists():
            raise Http404()

    if order_by and order_by != "default":
        products = products.order_by(order_by)

    if on_sale:
        products = products.filter(discount__gt=0)
    if new:
        products = products.filter(is_new=True)
    # if favorites:
    #     products = products.filter()

    paginator = Paginator(products, 12)
    current_page = paginator.page(int(page))

    total_pages = paginator.num_pages
    start = max(1, page - 1)
    end = min(total_pages, page + 1)

    if (end - start) < 2:
        if start == 1:
            end = min(total_pages, start + 2)
        elif end == total_pages:
            start = max(1, end - 2)

    context = {
        "products": current_page,
        "slug_url": category_slug,
        "page_range_start": start,
        "page_range_end": end,
    }

    if category_slug:
        context["category"] = Categories.objects.get(slug=category_slug)

    return render(request, "goods/catalog.html", context=context)


class ProductView(DetailView):

    template_name = "goods/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=...):
        return get_object_or_404(
            Products,
            slug=self.kwargs.get(self.slug_url_kwarg),
            is_active=True,
            category__is_active=True
        )
