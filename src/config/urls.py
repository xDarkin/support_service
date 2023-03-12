from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Support API",
        default_version="",
        description="Educational test OpenAPI",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

openapi_urls = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
v1 = [
    path("admin/", admin.site.urls),
    path("exchange-rates/", include("exchange_rates.urls")),
    path("", include("core.urls")),
    path("users/", include("users.urls")),
    path("auth/", include("authentication.urls")),
    # path("static/<path:path>/", serve, {"document_root": settings.STATIC_ROOT}),
]

urlpatterns = [
    path("v1/", include(v1)),
    path("", include(openapi_urls)),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()  # type:ignore
