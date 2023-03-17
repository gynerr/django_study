from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
from app_profiles.models import Profile


class Product(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    description = models.TextField(max_length=100, verbose_name=_('description'))
    price = models.PositiveIntegerField(verbose_name=_('price'))

    class Meta:
        ordering = ['title']
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return f'{self.title}'


class Shop(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    product = models.ManyToManyField(Product)

    class Meta:
        verbose_name = _('shop')
        verbose_name_plural = _('shops')

    def __str__(self):
        return self.title


class Check(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_of_sale = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.product} {self.shop} {self.profile} {self.date_of_sale.strftime("%d/%m/%y")}'
