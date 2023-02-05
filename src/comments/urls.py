from comments.api import CommentAPISet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"", CommentAPISet)

urlpatterns = [
    path("tickets/<int:ticket_id>/comments/", include(router.urls)),
]
