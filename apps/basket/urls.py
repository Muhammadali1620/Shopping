from django.urls import path

from . import views


urlpatterns = [
    path('', views.BaskedListAPIView.as_view()),
    path('<int:pk>/', views.CreateOrDeleteBaskedAPIView.as_view()),
]