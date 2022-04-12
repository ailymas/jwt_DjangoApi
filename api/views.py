from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView 
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from api.serializer import MyTokenObtainPairSerializer, RegisterSerializer,NotesSerializer
from rest_framework.decorators import api_view, permission_classes
from .models import Notes

# Create your views here.


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_class=(IsAuthenticated)
    serializer_class=RegisterSerializer

@api_view(['Get'])
def getRoutes(request):
    routes=[
        'api/token',
        'api/register',
        'api/refresh'
    ]
    return Response(routes)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user=request.user
    notes=user.note_set.all()
    serializer=NotesSerializer(notes,many=True)
    return Response(serializer.data)


