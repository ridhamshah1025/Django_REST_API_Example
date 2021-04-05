from django.shortcuts import render
from rest_framework.viewsets import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.views.decorators.csrf import csrf_exempt



class login_api(APIView):
    def post(self, request):
        serializer = login_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            # user = User(username=username, password=password)
            # user.save()
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({"Token": token.key})
            else:
                return Response({"message": "username or password is not valid"}, status=401)
        else:
            return Response({"message": serializer.errors}, status=401)


class logout_api(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response({"message":"Successfully Logout"})


class register_api(ModelViewSet):
    serializer_class = register_serializer
    queryset = User.objects.all()
