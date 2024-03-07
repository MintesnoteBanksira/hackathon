# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnterpriseViewSet, OrganizationViewSet, ServiceViewSet

router = DefaultRouter()
router.register(r'enterprises', EnterpriseViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]