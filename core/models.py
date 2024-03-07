from django.db import models
from django.contrib.auth.models import User

class Enterprise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)
    # Add more fields as needed

class Organization(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    # Add more fields as needed

class Service(models.Model):
    SERVICE_TYPES = [
        ('CB', 'ChatBot'),
        ('FAQ', 'FAQ'),
        ('CL', 'Calling'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)
    service_type = models.CharField(max_length=3, choices=SERVICE_TYPES, default='CB')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    # Add more fields as needed
