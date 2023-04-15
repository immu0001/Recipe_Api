"""
Test for Recipe API.
"""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import RecipeSerializer


RECIPE_URL = reverse('recipe:recipe-list')

def create_recipe(user, **params):
    """Create and return a sample recipe."""
    defaults = {
        'title': 'Sample Recipe Title',
        'time_minutes': 22,
        'price': Decimal('5.25'),
        'description': 'Sample Recipe Description',
        'link': 'http://example.com/recipe.pdf',
    }
    defaults.update(params) # If params is empty, defaults to above 'defaults'
    #OR else defaults.update(params) will update default values to values passed in from 'params'

    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe

class PublicRecipeAPITests(TestCase):
    """Test Unauthenticated API Requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_reuired(self):
        """Test Auth required to call API."""
        res = self.client.get(RECIPE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateRecipeAPITests(TestCase):
    """Test Authenticated API requests."""

    def setUp():
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'testpass123',
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_recipes(self):
        """Test retrieving a list of recipes."""
        create_recipe(user=self.user)
        create_recipe(user=self.user)

        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_recipe_list_limited_to_user(self):
        """Test list of recipes is limited to Autherised User."""
        other_user = get_user_model().objects.create_user(
            'otherUser@example.com',
            'password123',
        )
        create_recipe(user=other_user)
        create_recipe(user=self.user)

        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.filter(user=self.user)
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
