from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.CustomUserRegisterAPIView.as_view(), name='register'),
    path('login/', views.CustomUserLoginAPIView.as_view(), name='login'),
    path('', views.CustomUserListAPIView.as_view()),
]