from django.contrib import admin
from .models import Product, Customer, OrderRow, Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(OrderRow)
admin.site.register(Order)