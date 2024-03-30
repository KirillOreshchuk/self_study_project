from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """Права доступа для владельца"""
    massage = 'Вы не являетесь владельцем'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


class IsCurrentUser(BasePermission):
    """Права доступа для текущего пользователя"""
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.pk == request.user.pk


class IsStaffOrSuperuser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True
