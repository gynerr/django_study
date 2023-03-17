from datetime import datetime
from django.db import transaction
from django.db.models import F

from app_profiles.models import Profile
from shop.models import Shop, Product, Check


@transaction.atomic
def buy_select_product(request, shop_id, product_id):
    products = Shop.objects.get(id=shop_id).product # ManytoManyManager
    current_product = Product.objects.get(id=product_id)
    products.remove(current_product)
    profile = Profile.objects.filter(user=request.user)
    profile.update(balance=F('balance') - current_product.price)
    profile.update(spent_balance=F('spent_balance') + current_product.price)
    Check.objects.create(product=current_product, shop=Shop.objects.get(id=shop_id), profile=profile.first())
    if profile.first().spent_balance <= 1000:
        profile.update(status='be')
    elif 1000 <= profile.first().spent_balance <= 10000:
        profile.update(status='ad')
    elif profile.first().spent_balance > 10000:
        profile.update(status='ex')
