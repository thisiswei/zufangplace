from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, obj, request, view):
        return request.method in (permissions.SAFE_METHODS) or request.user == obj.user_profile
