from rest_framework.permissions import BasePermission
from . models import Bucketlist

class IsOwner(BasePermission):
    """Custom permission class to restrict bucketlist access to owners"""

    def has_object_permission(self, request, view, obj):
        """Returns true if permission is granted to owner"""
        if isinstance(obj, Bucketlist):
            return obj.owner == request.user
        return obj.owner == request.user
