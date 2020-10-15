from rest_framework import serializers
from .models import Register

class serializerpersons(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = '__all__'
