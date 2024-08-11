from rest_framework import serializers

from apps.basket.models import Basket
from apps.products.serializers import ProductSerializer


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = ['id', 'user', 'product', 'quantity']
