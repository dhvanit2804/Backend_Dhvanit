from django.shortcuts import render
from django.contrib.auth.models import User
import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from django.conf import settings
from google.auth.transport import requests
from google.oauth2 import id_token
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import Role, UserRole
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import HasRole

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username= request.data.get('username')
        password= request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_serializer.data
            })
        else:
            return Response({'error': 'Invalid Credentials'}, status=400)

class DashboardView(APIView):
    permission_classes = [IsAuthenticated, HasRole]
    required_role = 'python developer'

    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(user)
        return Response({'message': 'Welcome to the dashboard!', 'user': user_serializer.data}, status=200)


class GoogleAuthView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        id_token_value = request.data.get('id_token')
        access_token_value = request.data.get('access_token')
        if not id_token_value and not access_token_value:
            return Response({'error': 'id_token or access_token is required'}, status=400)

        google_client_id = getattr(settings, 'GOOGLE_OAUTH_CLIENT_ID', '')
        if not google_client_id:
            return Response({'error': 'Google OAuth client id is not configured on server'}, status=500)

        if id_token_value:
            try:
                payload = id_token.verify_oauth2_token(id_token_value, requests.Request(), google_client_id)
            except ValueError:
                return Response({'error': 'Invalid Google id_token'}, status=400)
        else:
            try:
                userinfo_request = Request(
                    'https://www.googleapis.com/oauth2/v3/userinfo',
                    headers={'Authorization': f'Bearer {access_token_value}'},
                )
                with urlopen(userinfo_request, timeout=10) as userinfo_response:
                    payload = json.loads(userinfo_response.read().decode('utf-8'))
            except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
                return Response({'error': 'Invalid Google access_token'}, status=400)

        email = payload.get('email')
        if not email:
            return Response({'error': 'Google account email is missing'}, status=400)

        base_username = (email.split('@')[0] or 'googleuser')[:150]
        username = base_username
        counter = 1

        while User.objects.filter(username=username).exclude(email=email).exists():
            suffix = str(counter)
            username = f"{base_username[:150-len(suffix)]}{suffix}"
            counter += 1

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'username': username,
                'first_name': payload.get('given_name', ''),
                'last_name': payload.get('family_name', ''),
            }
        )

        if created:
            role, _ = Role.objects.get_or_create(name='user')
            UserRole.objects.get_or_create(user=user, role=role)

        refresh = RefreshToken.for_user(user)
        user_serializer = UserSerializer(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': user_serializer.data,
            'created': created,
        })