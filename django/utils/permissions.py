from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission that permits authenticated users to view, and Admins to modify.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS and (request.user and request.user.is_authenticated()):
            return True
        else:
            return (request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
         return self.has_permission(request, view)


class UserListAndCreatePermissions(permissions.BasePermission):
    """
    Grants the following permissions:
        GET: Authenticated and Admin
        PUT: Self and Admin
        POST: Unauthenticated and Admin
        DELETE: Self and Admin
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True
        if request.method in permissions.SAFE_METHODS and (request.user and request.user.is_authenticated()):
            return True
        if request.method == 'POST':
            return True if not (request.user and request.user.is_authenticated()) or request.user.is_staff else False
        return False
