from django.urls import include, path
from rest_framework import routers
from tickets.api import TicketAPISet

router = routers.DefaultRouter()
router.register(r"", TicketAPISet)

urlpatterns = [
    path("", include(router.urls)),
]
