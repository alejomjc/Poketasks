from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views
from rest_framework import authentication

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="Your API description here",
      terms_of_service="https://www.yourapp.com/terms/",
      contact=openapi.Contact(email="alejomjc2011@gmail.com"),
      license=openapi.License(name="Your License"),
   ),
    public=False,
    permission_classes=[permissions.IsAuthenticated],
    authentication_classes=[authentication.TokenAuthentication, authentication.SessionAuthentication],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Pokemon.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-token-auth/', views.obtain_auth_token),
    path('', admin.site.urls),
]
