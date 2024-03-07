# users/urls.py
from django.urls import path
from .views import RegisterAPIView , LoginView , LogoutView , RetrieveUser , HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('user/register', RegisterAPIView.as_view(), name='register'),
    path('user/login', LoginView.as_view(), name='login'),
    path('user/logout', LogoutView.as_view(), name='logout'),
    path('', RetrieveUser.as_view(), name='retrieve'),


]