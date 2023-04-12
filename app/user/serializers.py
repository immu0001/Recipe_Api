"""
Serializers for the user API View.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    #  serializers.ModelSerializer is used to serialize this class bcz
    #  we want to serialize and then covert the JSON to a model object.
    """Serializer for the user Object."""

    class Meta:
        #  this is where we tell the django framework the models and the fields
        #  and any additional fields that we want to pass to the serializer.
        model = get_user_model() # telling serializer that which model it has to use for this operation.
        fields = ['email', 'password', 'name'] # fields that should be saved in the model object
        extra_kwargs = {'password': {'write_only': True, 'min_length':5}}

        def create(self, validated_data):
            """Create and return the user object with ecrypted password."""
            return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user Authentication Token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace = False,
    )

    def validate(self, attrs):
        """ Validate and Authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username = email,
            password = password,
        )
        if not user:
            msg = _("Unable to Authenticate with provided credentials.")
            raise serializers.ValidationError(msg, code = 'authorization')

        attrs['user'] = user
        return attrs
