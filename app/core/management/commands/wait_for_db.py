"""

Django Command to wait for the database to be available.

"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django Command to wait for the Database. """

    def handle(self, *args, **options):
        pass