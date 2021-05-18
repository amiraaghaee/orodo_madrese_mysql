from rest_framework import serializers
from .models import Product, Customer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "code", "name", "price", "inventory"]


# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ["id", "username", "first_name", "last_name", "email", "phone", "address", "balance"]