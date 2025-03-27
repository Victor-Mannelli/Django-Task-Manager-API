from task_manager.serializers import RegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status

# Class-Based Views (CBV)
class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully!"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    # It is used to generate new access tokens without re-logging in.
                    "refresh": str(refresh),
                    # It grants access to protected routes.
                    "access": str(refresh.access_token), 
                }
            )
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "Logged out successfully"}, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )
