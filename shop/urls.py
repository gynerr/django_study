from django.urls import path

from shop.views import ProductListView, StatisticView

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product-list'),
    path('statistic/', StatisticView, name='statistic'),
]