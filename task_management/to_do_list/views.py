from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets

# Create your views here.


class UserTaskViewSet(viewsets.ModelViewSet):
    queryset = models.UserTask.objects.select_related('user')
    serializer_class = serializers.UserTaskSerializer
