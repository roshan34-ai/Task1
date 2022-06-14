from rest_framework.permissions import BasePermission 
from .models import CustomUser, Task


class IsTeamLeader(BasePermission):
   
    def has_permission(self, req, view):
        user=req.user.name
        User=CustomUser.objects.get(name=user)
        Role = User.role
        if Role==1 :
            return True
        return False


class IsTeamMembar(BasePermission):
   
    def has_object_permission(self, req, view, obj):
        user=req.user.name
        User=CustomUser.objects.get(name=user)
        task=Task.objects.get(name=obj)
        Role = User.role
        Status=task.status
        if Role==2:
            Status=task.status
            return Status
        return False

