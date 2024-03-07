from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return self.user.username
