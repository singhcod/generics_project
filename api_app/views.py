from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from api_app.serializers import EmployeeSerializer
from api_app.models import Employee

class EmployeeGerincView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer