from rest_framework.permissions import BasePermission


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_role('admin')


class IsModeratorPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_role('moderator')


class IsUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_role('user')
