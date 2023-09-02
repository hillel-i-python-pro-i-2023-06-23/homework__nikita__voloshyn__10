from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create a superuser with username "admin" and password "admin123"'

    def handle(self, *args, **kwargs):
        username = "admin"
        password = "admin123"

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'Superuser with username "{username}" already exists.'))
            return

        User.objects.create_superuser(username=username, password=password)
        self.stdout.write(
            self.style.SUCCESS(f'Superuser "{username}" with password "{password}" created successfully.')
        )
