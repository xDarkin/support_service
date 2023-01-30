from rest_framework.permissions import BasePermission
from users.constants import Role
from django.contrib.auth import get_user_model

User = get_user_model()


class RoleIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.ADMIN


class RoleIsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.MANAGER


class RoleIsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.USER


class UserOwner(BasePermission):
    def has_object_permission(self, request, view, obj: User):
        return obj.email == request.user.email
