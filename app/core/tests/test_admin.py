"""
Tests for the Django admin Modifications.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTests(TestCase):
    """ Tests for Django admin."""

    def setUp(self) -> None:
        """ Create User and Client."""
        self.client = Client()
