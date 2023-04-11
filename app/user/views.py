"""
Views for the user API.

"""
from rest_framework import generics

from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    # generics.CreateAPIView handles HTTP post request thats designed for creating objects in the DB.
    """
    Create a new user in the System.
    """
    serializer_class = UserSerializer
