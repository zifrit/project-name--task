from rest_framework import serializers
from . import models


class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserTask
        fields = '__all__'
