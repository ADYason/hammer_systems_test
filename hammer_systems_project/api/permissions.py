from rest_framework import permissions


class Verified(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.confirmed
