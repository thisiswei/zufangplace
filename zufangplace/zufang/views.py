from rest_framework import viewsets
from rest_framework import permissions

from .permissions import IsOwner
from .permissions import IsPictureFang
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


class PictureViewSet(viewsets.ModelViewSet):
    queryset = models.Picture.objects.all()
    serializer_class = serializers.PictureSerializer
    permission_classes = (
        IsPictureFang,
        permissions.IsAuthenticatedOrReadOnly,
    )


class LikeViewSet(viewsets.ModelViewSet):
    queryset = models.Like.objects.all()
    serializer_class = serializers.LikeSerializer
