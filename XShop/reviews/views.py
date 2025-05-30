from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from goods.models import Products
from orders.models import OrderItem
from reviews.forms import ReviewForm
from reviews.models import Review


class ReviewCreateView(FormView):
    form_class = ReviewForm

    def form_valid(self, form):
        user = self.request.user
        product_id = self.request.POST.get("product_id")

        if not product_id:
            form.add_error(None, "Product not specified.")
            return self.form_invalid(form)

        product = get_object_or_404(Products, id=product_id)

        # Проверка: куплен ли товар этим пользователем
        has_purchased = OrderItem.objects.filter(
            order__user=user,
            order__status="Completed",
            product=product
        ).exists()

        if not has_purchased:
            form.add_error(None, "You can only review purchased products.")
            return self.form_invalid(form)

        # Проверка: уже оставлен отзыв?
        if Review.objects.filter(user=user, product=product).exists():
            form.add_error(None, "You have already submitted a review.")
            return self.form_invalid(form)

        # Сохраняем отзыв
        review = form.save(commit=False)
        review.user = user
        review.product = product
        review.save()

        return redirect(self.get_success_url(product))

    def form_invalid(self, form):
        product_id = self.request.POST.get("product_id")
        if product_id:
            product = get_object_or_404(Products, id=product_id)
            return redirect(reverse("catalog:product", kwargs={"product_slug": product.slug}))
        return super().form_invalid(form)

    def get_success_url(self, product):
        return reverse("catalog:product", kwargs={"product_slug": product.slug})


class ReviewEditView(View):
    pass


class ReviewDeleteView(View):
    pass