from django.shortcuts import render
from rest_framework import viewsets
from .models import Routes
from .serializers import RouteSerializer
# Create your views here.

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Routes.objects.all()
    serializer_class = RouteSerializer