from datetime import datetime

from django.db.models import Count, Max
from django.shortcuts import render
# Create your views here.
from django.utils import timezone
from django.views import generic

from shop.models import Product, Check


class ProductListView(generic.ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'

def StatisticView(request):
    product = Product.objects.filter(check__date_of_sale__gte=datetime(2023, 3, 12, 0, 0, 0)).annotate(count_in_check=Count('check'))
    return render(request, 'shop/statistic.html', {'product': product})