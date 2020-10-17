from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# from django.contrib.auth import get_user_model
from .models import profile, User, sell, buy, article

# User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('email','username','phone','password')
        extra_kwargs = {
            'password':{'write_only': True}
        }

    def create (self,data):
        user = User.objects.create_user(**data)
        return user

# class ProfilesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = profile
#         fields = ('first_name', 'last_name', 'address')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = ('first_name', 'last_name', 'address')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = ('name', 'price', 'description')

class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = buy
        fields = '__all__'

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = sell
        fields = '__all__'
