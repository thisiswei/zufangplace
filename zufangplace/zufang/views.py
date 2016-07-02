from rest_framework import viewsets
from rest_framework import permissions

from .permissions import IsOwner
from . import models
from . import serializers


class FangViewSet(viewsets.ModelViewSet):
    queryset = models.Fang.objects.all()
    serializer_class = serializers.FangSerializer
    permission_classes = (
        IsOwner,
        permissions.IsAuthenticatedOrReadOnly,
    )


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSeriazlier
