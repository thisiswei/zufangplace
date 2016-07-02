from rest_framework import serializers

from .models import UserProfile
from .models import Fang


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
        model = UserProfile
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

    class Meta:
        model = Fang
        fields = (
            'url',
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
