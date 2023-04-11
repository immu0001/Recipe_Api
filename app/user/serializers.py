"""
Serializers for the user API View.
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    #  serializers.ModelSerializer is used to serialize this class bcz
    #  we want to serialize and then covert the JSON to a model object.
    """Serializer for the user Object."""

    class Meta:
        #  this is where we tell the django framework the models and the fields
        #  and any additional fields that we want to pass to the serializer.
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length':5}}

        def create(self, validated_data):
            """Create and return the user object with ecrypted password."""
            return get_user_model().objects.create(**validated_data)
