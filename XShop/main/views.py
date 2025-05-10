from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Products
import random


class IndexView(TemplateView):
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        products = list(Products.objects.filter(is_active=True, category__is_active=True))
        random.shuffle(products)
        
        context['recommended_products'] = products[:4]
        
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'


class DeliveryView(TemplateView):
    template_name = 'main/delivery.html'


class PolicyView(TemplateView):
    template_name = 'main/policy.html'


class TermsView(TemplateView):
    template_name = 'main/terms.html'


class OrdandretView(TemplateView):
    template_name = 'main/ordandret.html'

