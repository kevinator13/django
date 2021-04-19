from django.shortcuts import render
from rest_framework import viewsets
from .models import App
from .serializers import AppSerializer
# Create your views here.

class AppView(viewsets.ModelViewSet):
	queryset = App.objects.all()
	serializer_class = AppSerializer