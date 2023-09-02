from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create a superuser automatically"

    def handle(self, *args, **options):
        UserModel = get_user_model()

        username = "admin"
        password = "admin123"
        email = "admin@example.com"

        if not UserModel.objects.filter(username=username).exists():
            user = UserModel.objects.create_user(username=username, email=email, password=password)
            user.is_superuser = True
            user.is_staff = True
            user.save()

        self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
