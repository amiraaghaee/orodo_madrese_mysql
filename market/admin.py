from django.contrib import admin
from .models import Product, OrderRow, Order
# Register your models here.

admin.site.register(Product)
admin.site.register(OrderRow)
admin.site.register(Order)