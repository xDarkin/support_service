from django.urls import include, path
from rest_framework import routers
from users.api import UserAPISet

router = routers.DefaultRouter()
router.register(r"", UserAPISet)

urlpatterns = [
    path("", include(router.urls)),
]
