from datetime import datetime, timedelta
import jwt
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from .models import UserProfile
from .serializers import UserProfileSerializer, UserSerializer

# Home View
def home(request):
    return HttpResponse("Welcome to Paysphere! Hello, This is Jack")

# JWT Token Generation
def generate_jwt_token(user):
    payload = {
        "user_id": user.id,
        "role": user.role,
        "exp": datetime.utcnow() + timedelta(hours=2),
        "iat": datetime.utcnow()
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token

# Custom JWT Authentication
class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header or " " not in auth_header:
            return None  
        
        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = UserProfile.objects.get(id=payload["user_id"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired.")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token.")
        except UserProfile.DoesNotExist:
            raise AuthenticationFailed("User not found.")

        return (user, token)

# User Login View
class CustomLoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = UserProfile.objects.get(email=email)
            if not check_password(password, user.password):
                raise AuthenticationFailed("Incorrect password.")
        except UserProfile.DoesNotExist:
            raise AuthenticationFailed("User not found.")

        token = generate_jwt_token(user)

        return Response({"message": "Login successful", "token": token, "role": user.role}, status=status.HTTP_200_OK)

# User Registration View
class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = generate_jwt_token(user)
            return Response({"message": "User registered successfully", "token": token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Management ViewSet
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role.lower() == "hr":
            return UserProfile.objects.all()
        return UserProfile.objects.filter(id=user.id)

# Activate User
class ActivateUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, user_id):
        try:
            user = UserProfile.objects.get(id=user_id)
            if not request.user.role or request.user.role.lower() != "hr":
                return Response({"error": "Only HR can activate users."}, status=status.HTTP_403_FORBIDDEN)

            user.is_active = True
            user.save()
            return Response({"message": "User activated successfully."}, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

# Deactivate User
class DeactivateUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, user_id):
        try:
            user = UserProfile.objects.get(id=user_id)
            if not request.user.role or request.user.role.lower() != "hr":
                return Response({"error": "Only HR can deactivate users."}, status=status.HTTP_403_FORBIDDEN)

            user.is_active = False
            user.save()
            return Response({"message": "User deactivated successfully."}, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

# Update User Details
class UpdateUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, user_id):
        try:
            user = UserProfile.objects.get(id=user_id)
            if request.user.role.lower() != "hr" and request.user.id != user.id:
                return Response({"error": "Unauthorized action."}, status=status.HTTP_403_FORBIDDEN)

            serializer = UserProfileSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "User updated successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except UserProfile.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

# Fetch All Employees (For HR Only)
class GetAllEmployeesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role.lower() != "hr":
            return Response({"error": "Only HR can view all employees."}, status=status.HTTP_403_FORBIDDEN)

        employees = UserProfile.objects.all()
        serializer = UserProfileSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
