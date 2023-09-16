import os

from rest_framework import serializers

from ...model import Role


class RoleSerializer(serializers.Serializer):
    class Meta:
        model = Role
        fields = '__all__'


