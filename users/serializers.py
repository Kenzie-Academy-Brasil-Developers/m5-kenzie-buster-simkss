from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User



class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message="username already taken."
            )], max_length=20)
    email = serializers.EmailField(
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message="email already registered."
            )], max_length=127)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(allow_null=True, read_only=True)
    birthdate = serializers.CharField(allow_null=True, default=None)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        if validated_data["is_employee"] == True:
            return User.objects.create_superuser(**validated_data)

        self.is_employee = None
        self.is_superuser = None

        return User.objects.create_user(**validated_data)