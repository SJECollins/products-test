from django.shortcuts import render, get_object_or_404
from django.views import View, generic

from .models import BaseProduct, Seed, Sauce, SeedBox, SauceBox


class ProductsList(generic.ListView):
    model = BaseProduct
    queryset = BaseProduct.objects.all()
    template_name = 'index.html'


class SeedBoxView(View):
    def get(self, request, slug):
        seedbox = get_object_or_404(SeedBox, slug=slug)
        template_name = 'product.html'
        context = {
            'product': seedbox,
        }
        return render(request, template_name, context)