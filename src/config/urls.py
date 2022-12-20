from django.urls import include, path

urlpatterns = [
    path("exchange-rates/", include("exchange_rates.urls")),
]
