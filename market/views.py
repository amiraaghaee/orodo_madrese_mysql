"""
    You can define utility functions here if needed
    For example, a function to create a JsonResponse
    with a specified status code or a message, etc.

    DO NOT FORGET to complete url patterns in market/urls.py
"""

from django.http import Http404
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, )


@api_view(['GET', 'PUT', 'DELETE', 'UPDATE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404({"message": "Product Not Found."})

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        Product.inventory += ProductSerializer(product, data=request.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "UPDATE"])
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            Product.inventory += ProductSerializer(product, data=request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST), Http404({"message": "Product Not Found."})
