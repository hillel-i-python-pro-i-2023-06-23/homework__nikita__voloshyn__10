from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Contact
from faker import Faker

class Command(BaseCommand):
    help = 'Populate data with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            user, created = User.objects.get_or_create(
                username=fake.user_name(),
                defaults={'password': fake.password()}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'User "{user.username}" created successfully'))
            else:
                self.stdout.write(self.style.SUCCESS(f'User "{user.username}" already exists'))

            contact = Contact.objects.create(
                user=user,
                name=fake.name(),
                email=fake.email(),
                phone_number=fake.phone_number()
            )

            self.stdout.write(self.style.SUCCESS(f'Data for user "{user.username}" populated successfully'))
