from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name='products'),
    path('<int:pk>', views.ProductDetailAPIView.as_view()),
]