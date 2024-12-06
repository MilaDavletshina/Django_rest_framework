from rest_framework.permissions import BasePermission


#10.5
class IsOwnerOrStaff(BasePermission):
    """Проверка на менеджера и владельца"""
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.user == view.get_object().owner