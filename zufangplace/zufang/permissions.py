from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in (permissions.SAFE_METHODS) or request.user == obj.user_profile


class IsPictureFang(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in (permissions.SAFE_METHODS) or request.user.id == obj.fang.user_profile.id
