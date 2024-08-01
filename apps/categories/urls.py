from django.urls import path

from . import views


urlpatterns = [
    path('', views.CategoryListAPIView.as_view(), name='categories'),
]