from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductListAPIView(APIView):
    def get(self, request, format=None):
        category_id = request.GET.get('category_id', '')
        products = Product.objects.all().prefetch_related('images').select_related('category')
        if category_id:
            products = products.filter(category_id=category_id)
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


class ProductDetailAPIView(APIView):
    def get(self, request, pk, format=None):
        if not Product.objects.filter(pk=pk).exists():
            return Response({'error': 'Bad request'})
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)
