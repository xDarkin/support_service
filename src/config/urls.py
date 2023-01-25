from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("exchange-rates/", include("exchange_rates.urls")),
    path("", include("core.urls")),
    path("users/", include("users.urls")),
]
