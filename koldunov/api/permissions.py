# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class ReadOnly(BasePermission):
    """
    Object-level permission to only allow only read object.
    """
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return False
