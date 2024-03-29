from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

schema_view = get_schema_view(
   openapi.Info(
      title="Banco Stone API",
      default_version='v1',
      description="A REST API that was developed as a chalenge from Stone Tech, "
                  "as a conclusion of the Codigo[s] Bootcamp",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="costa.camila.ro@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('transactions.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('swagger<format>.json|.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
