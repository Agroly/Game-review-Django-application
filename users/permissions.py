from rest_framework.permissions import BasePermission


class IsEditorPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_role('moderator') or request.user.has_role('admin')

