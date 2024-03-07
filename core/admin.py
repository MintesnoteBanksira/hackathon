from django.contrib import admin
from .models import Enterprise, Organization, Service

admin.site.register(Enterprise)
admin.site.register(Organization)
admin.site.register(Service)