from vessels.models import Vessel
from vessels.serializers import VesselSerializer
from rest_framework import generics

#for authentication
from rest_framework import permissions
from django.contrib.auth.models import User
from vessels.serializers import UserSerializer

#for API endpoint
from rest_framework.decorators import api_view
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'vessels': reverse('vessel-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
    })

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VesselList(generics.ListCreateAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VesselDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
