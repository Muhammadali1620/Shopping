from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductListAPIView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all().prefetch_related('images')
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


class ProductDetailAPIView(APIView):
    def get(self, request, pk, format=None):
        if not Product.objects.filter(pk=pk).exists():
            return Response({'error': 'Bad request'})
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)
