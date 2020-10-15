from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'phone')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, data):
        user = User.objects.create_user(**data)
        return user
