from rest_framework import serializers

from apps.categories.serializers import CategorySerializer
from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request is not None:
            representation['image'] = request.build_absolute_uri(instance.image.url)
        else:
            representation['image'] = instance.image.url
        return representation


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'title', 'slug', 'price', 'sale_price', 'desc', 'created_at', 'updated_at', 'images']
