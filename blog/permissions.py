from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_active

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return (request.user.is_authenticated and request.user.is_active and request.user==obj.author)
