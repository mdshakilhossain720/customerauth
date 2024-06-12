from django.shortcuts import render
from .models import Student
from .serilazers import StudentSerlazers
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication,SessionAuthentication
from.custompermission import MyPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throutilling import JackRateThrouting

from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions


# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerlazers
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,UserRateThrottle,UserRateThrottle]

    # authentication_classes=[SessionAuthentication]
    # permission_classes=[MyPermission]
    #permission_classes=[IsAuthenticated]
    # permission_classes=[IsAuthenticatedOrReadOnly]
   # permission_classes=[DjangoModelPermissions]
   

    




    # authentication_classes=[BaseAuthentication]
    # permission_classes=[IsAuthenticated]

# class StudentModelViewSet1(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerlazers
#     authentication_classes=[BaseAuthentication]
#     permission_classes=[AllowAny]

# class StudentModelViewSet2(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerlazers


# class StudentModelViewSet3(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerlazers


# class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerlazers

