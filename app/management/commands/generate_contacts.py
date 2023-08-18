from django.core.management.base import BaseCommand
from faker import Faker
from app.models import Contact

fake = Faker()


class Command(BaseCommand):
    help = "Generate random contacts"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, default=10, help="Number of contacts to generate")

    def handle(self, *args, **options):
        count = options["count"]

        for _ in range(count):
            Contact.objects.create(
                first_name=fake.first_name(),
                phone=fake.phone_number(),
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully generated {count} contacts"))
