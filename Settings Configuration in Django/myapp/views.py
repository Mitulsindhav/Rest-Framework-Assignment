from django.shortcuts import render
from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer


# Create your views here.

class DoctorList(generics.ListCreateAPIView):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer

class DoctorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Doctor
    serializer_class=DoctorSerializer
        