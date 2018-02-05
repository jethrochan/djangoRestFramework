from rest_framework import serializers
from .models import Vessel
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    #vessels = serializers.PrimaryKeyRelatedField(many=True, queryset=Vessel.objects.all())
    vessels = serializers.HyperlinkedRelatedField(many=True, view_name='vessel-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'vessels')

class VesselSerializer(serializers.HyperlinkedModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Vessel
        fields = ('url', 'id', 'created', 'name', 'description', 'size', 'color', 'owner',)
