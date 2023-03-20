from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from shop.views import ProductListView, StatisticView

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product-list'),
    path('statistic/', StatisticView, name='statistic'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)