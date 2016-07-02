from rest_framework import serializers

from . import models


class UserProfileSeriazlier(serializers.HyperlinkedModelSerializer):
    fangs = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='fang-detail',
        read_only=True,
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='userprofile-detail',
    )
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = models.UserProfile
        fields = (
            'url',
            'phone',
            'fangs',
            'username',
        )


class FangSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='fang-detail',
    )
    pictures = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='picture-detail',
        read_only=True,
    )

    class Meta:
        model = models.Fang
        fields = (
            'url',
            'pictures',
            'is_studio',
            'num_bedroom',
            'num_bathroom',
            'date_avaialable',
            'price_rent',
            'price_buy',
            'zipcode',
            'street',
            'city',
            'state',
            'country',
            'lat',
            'lon',
            'active',
        )


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='picture-detail',
    )

    class Meta:
        model = models.Picture
        fields = (
            'url',
            'name',
        )
