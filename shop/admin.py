from django.contrib import admin

# Register your models here.
from shop.models import Shop, Product, Check

admin.site.register(Shop)
admin.site.register(Product)
@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    readonly_fields = ['date_of_sale']
