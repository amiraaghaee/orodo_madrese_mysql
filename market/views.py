from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from knox.models import AuthToken
from rest_framework.response import Response
from .models import *
from .serializers import ProductSerializer, UserSerializer, RegisterSerializer
from rest_framework import generics, permissions
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer


def product_list(request):
    if request.method == "GET":
        allProduct = Product.objects.all()
        serializer = ProductSerializer(allProduct, many=True)
        return JsonResponse({"products": serializer.data}, status=200)
    else:
        return JsonResponse(({"message": "Duplicate code (or other messages)"}), status=400)


def product_insert(request):
    if request.method == "POST":
        data1 = JSONParser().parse(request)
        serializer = ProductSerializer(data=data1)
        product = Product.objects.filter(code=data1["code"])
        if product.exists():
            return JsonResponse({"message": "Duplicate code (or other messages)"}, status=400)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"products": serializer.data}, status=201)
    return JsonResponse(({"message": "Duplicate code (or other messages)"}), status=400)


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Product Not Found."}, status=404)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)


def product_search(request):
    try:
        detail = request.query_params['search']
        product = Product.objects.get(pk=detail)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Product Not Found."}, status=404)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data, status=200)


def product_update(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Product Not Found."}, status=404)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
#edit