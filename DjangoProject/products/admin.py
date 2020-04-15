from django.contrib import admin
from .models import Product, Offer


# This is what we need to add so when whe are on the admin's page we can see the stock by name
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
