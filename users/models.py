from django.contrib.auth.models import AbstractUser
from django.db import models
# from rest_framework.permissions import BasePermission

# Create your models here.
class User(AbstractUser):
    """
    User model with role-based access
    """

    ROLE_CHOICES = [
        ('super_admin', 'Super Admin'),
        ('secretariat', 'Secretariat'),
        ('therapist', 'Therapist'),
        ('guardian', 'Guardian'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='guardian')

    def _str_(self):
        return f"{self.username} - {self.role}"
    

# class IsSuperAdmin(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.role == 'super_admin'
    