# from rest_framework import permissions
#
#
# class IsResponsable(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         return (request.method in permissions.SAFE_METHODS or
#                 request.user.is_authenticated and
#                 request.user.is_freelancer or
#                 request.user.is_superuser)
#
#     def has_object_permission(self, request, view, obj):
#         return (request.method in permissions.SAFE_METHODS or
#                 request.user.is_authenticated and
#                 request.user.is_freelancer or
#                 request.user.is_superuser)
#
#
# class IsAuthor(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         return (request.method in permissions.SAFE_METHODS or
#                 request.user.is_authenticated and
#                 request.user.is_customer)
#
#     def has_object_permission(self, request, view, obj):
#         return (request.method in permissions.SAFE_METHODS and
#                 request.user.is_customer or
#                 obj.author == request.user)

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.is_customer

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return obj.author == request.user


class IsResponsable(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.is_freelancer
