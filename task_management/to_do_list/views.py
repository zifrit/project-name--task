from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.UserTask.objects.select_related('user')
    serializer_class = serializers.UserTaskSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter
    ]
    search_fields = [
        "name"
    ]
    filterset_fields = [
        'name',
        'user__username',
        'archive'
    ]
    ordering_fields = [
        'name'
    ]

    def list(self, request, *args, **kwargs):
        query = super(TaskViewSet, self).get_queryset()
        print(query)
        data = serializers.UserTaskSerializer(instance=query, many=True).data
        return super(TaskViewSet, self).list(request, *args, **kwargs)


class UserTask(generics.ListAPIView):
    serializer_class = serializers.UserTaskSerializer

    def get_queryset(self):
        a, b = models.UserTask.objects.get_or_create(user_id=1, name='123', description='123')
        return models.UserTask.objects.filter(user=self.request.user, archive=False).select_related('user')
