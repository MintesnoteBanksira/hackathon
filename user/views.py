from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .serializers import UserSerializer, UserProfileSerializer , UserAndProfileSerializer
from .models import UserProfile
from drf_yasg.utils import swagger_auto_schema
from .utils import generate_jwt_token, send_mail
from django.utils import timezone

from django.db import IntegrityError
@method_decorator(csrf_exempt, name="dispatch")
class RegisterAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Create a new User", request_body=UserAndProfileSerializer
    )
    @transaction.atomic
    def post(self, request):
        print("Starting post method")  # Debug print
        user_serializer = UserSerializer(data=request.data.get("user"))
        if user_serializer.is_valid():
            print("User serializer is valid")  # Debug print
            user = user_serializer.save()
            profile_data = request.data
            profile_data["user"] = user.id
            profile_serializer = UserProfileSerializer(data=profile_data)
            if profile_serializer.is_valid():
                print("Profile serializer is valid")  # Debug print
                profile = profile_serializer.save(user=user)

                
                profile.save()
                return Response(
                    {
                     "message": "User created successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                print("Profile serializer is not valid")  # Debug print
                user.delete()  # delete the user if profile creation fails
                return Response(
                    profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        print("User serializer is not valid")  # Debug print
        return Response(
            user_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
