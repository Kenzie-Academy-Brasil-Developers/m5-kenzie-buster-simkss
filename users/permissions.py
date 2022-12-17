from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == "GET":
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False

class IsAuthUser(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True

        return False