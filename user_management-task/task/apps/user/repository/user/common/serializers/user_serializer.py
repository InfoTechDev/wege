from django.contrib.auth import password_validation
from rest_framework import serializers

from task.apps.user.repository.user.model import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.FileField(required=False)

    class Meta:
        model = User
        fields ="__all__"
        extra_kwargs = {
            # 'email': {'validations': [UniqueValidator(queryset=User.objects.all(), message=msg_auth_00009)],
            #           "error_messages": {"required": msg_auth_00006, "blank": msg_auth_00006}},
            'password': {'write_only': True, 'required': True}
        }

    # def create(self, validated_data):
    #     validated_data = self.root.initial_data.copy()
    #     validated_data['username'] = ""
    #
    #     user = User.objects.create(**validated_data)
    #
    #     return user

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value