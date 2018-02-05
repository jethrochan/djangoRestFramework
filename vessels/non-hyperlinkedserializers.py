from rest_framework import serializers
from .models import Vessel
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    vessels = serializers.PrimaryKeyRelatedField(many=True, queryset=Vessel.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'vessels')

class VesselSerializer(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Vessel
        fields = ('id', 'created', 'name', 'description', 'size', 'color', 'owner',)
