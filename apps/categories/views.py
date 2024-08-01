from rest_framework.views import APIView
from rest_framework.response import Response

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


class CategoryListAPIView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
