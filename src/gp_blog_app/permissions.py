from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "You must be the owner of this blog !"

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
