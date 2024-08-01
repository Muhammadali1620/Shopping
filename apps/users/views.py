from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.permissions import IsAuthenticated

from apps.users.serializers import CustomUserRegisterSerializer, CustomUserLoginSerializer

UserModel = get_user_model()


class CustomUserRegisterAPIView(APIView):
    def post(self, request):
        serializer = CustomUserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class CustomUserListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = UserModel.objects.values('id', 'phone_number', 'full_name')
        return Response(data=users)


class CustomUserLoginAPIView(APIView):
    def post(self, request):
        serializer = CustomUserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=201)
