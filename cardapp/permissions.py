from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.owner is None:
            return True

        # returns True if the owner of the CookieStand is the requester
        return obj.owner == request.user