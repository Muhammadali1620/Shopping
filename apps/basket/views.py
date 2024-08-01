from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.basket.models import Basket
from apps.basket.serializers import BasketSerializer
from apps.products.models import Product


class BaskedListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        baskets = Basket.objects.filter(user_id=user.pk).select_related('product').prefetch_related('product__images')
        serializer = BasketSerializer(baskets, many=True, context={'request': request})
        return Response(serializer.data)


class CreateOrDeleteBaskedAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        user = request.user
        if not Product.objects.filter(pk=pk).exists():
            return Response({'error': 'Bad request'})
        basket, create = Basket.objects.get_or_create(user_id=user.pk, product_id=pk)
        message = 'Product successful added to basket'
        if not create:
            message = 'Product successful deleted to basket'
            basket.delete()
        return Response({'message': message})
