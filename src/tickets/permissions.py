from rest_framework.permissions import BasePermission
from users.constants import Role
from tickets.models import Ticket


class RoleIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.ADMIN


class RoleIsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.MANAGER


class TicketOwner(BasePermission):
    def has_object_permission(self, request, view, obj: Ticket):
        return obj.customer == request.user


class TicketManager(BasePermission):
    def has_object_permission(self, request, view, obj: Ticket):
        return obj.manager == request.user


class RoleIsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.USER
