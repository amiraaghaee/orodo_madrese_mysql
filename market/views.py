from django.http import JsonResponse
from .models import *
from .serializers import ProductSerializer


def product_list(request):
    if request.method == "GET":
        allProduct = Product.objects.all()
        serializer = ProductSerializer(allProduct, many=True)
        return JsonResponse({"products": serializer.data}, status=200)
    else:
        return JsonResponse(({"message": "Duplicate code (or other messages)"}), status=400)


def product_insert(request):
    if request.method == "POST":
        data1 = request.data
        serializer = ProductSerializer(data=data1)
        product = Product.objects.filter(code=data1["code"])
        if product.exists():
            return JsonResponse({"message": "Duplicate code (or other messages)"}, status=400)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"products": serializer.data.filter(id=data1["id"])}, status=201)
    return JsonResponse(({"message": "Duplicate code (or other messages)"}), status=400)


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Product Not Found."}, status=404)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)


def product_search(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Product Not Found."}, status=404)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

