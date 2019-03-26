from rest_framework import serializers
from .models import Dweet, Dweeter, Comment, Liked, FollowedDweeter


class DweetSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Dweet
        fields = ('id', 'dweeterId', 'text', 'likeCount', 'crDate',
                  'crBy', 'lmodDate', 'lmodBy', 'isActive')
        read_only_fields = ('crDate', 'crBy', 'lmodDate', 'lmodBy', 'isActive')


class DweeterSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Dweeter
        fields = ('id', 'username', 'pswd', 'fullname', 'country',
                  'crDate', 'crBy', 'lmodDate', 'lmodBy', 'isActive')
        read_only_fields = ('crDate', 'crBy', 'lmodDate', 'lmodBy', 'isActive')
        # extra_kwargs = {'username': {'required': True},
        #      'pswd': {'required': True}}


class CommentSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Comment
        fields = ('id', 'dweetId', 'commenterId', 'text', 'crDate',
                  'crBy', 'lmodDate', 'lmodBy', 'isActive')
        # read_only_fields = ('crBy')


class LikeSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Liked
        fields = ('id', 'dweetId', 'likedBy', 'crDate',
                  'crBy', 'lmodDate', 'lmodBy', 'isActive')
        # read_only_fields = ('crBy')


class FollowSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = FollowedDweeter
        fields = ('id', 'dweeterId', 'followerDweeterId', 'crDate',
                  'crBy', 'lmodDate', 'lmodBy', 'isActive')
        # read_only_fields = ('crBy')
