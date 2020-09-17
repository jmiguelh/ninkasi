from django.shortcuts import render
from rest_framework import viewsets
from .models import Empresa
from .serializers import EmpresaSerializers


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializers
