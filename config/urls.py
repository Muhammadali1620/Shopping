from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from .yasg import schema_view


urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('rest_api/', include('rest_framework.urls')),
    path('users/', include('apps.users.urls')),
    path('basket/', include('apps.basket.urls')),
    path('products/', include('apps.products.urls')),
    path('categories/', include('apps.categories.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
