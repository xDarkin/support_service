from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("exchange-rates/", include("exchange_rates.urls")),
    path("", include("core.urls")),
    path("users/", include("users.urls")),
    path("auth/", include("authentication.urls")),
    # path("static/<path:path>/", serve, {"document_root": settings.STATIC_ROOT})
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()  # type:ignore
