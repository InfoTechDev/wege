import os

from rest_framework import serializers

from ...model import Profile


class ProfileSerializer(serializers.Serialier):
    class Meta:
        model = Profile
        fields = '__all__'


