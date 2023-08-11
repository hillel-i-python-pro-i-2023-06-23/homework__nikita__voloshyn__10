import random
from faker import Faker
from django.core.management.base import BaseCommand
from app.models import Contact, ContactGroup, ContactType, ContactData

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with fake contacts'

    def handle(self, *args, **kwargs):
        # Create Contact Groups
        contact_groups = [ContactGroup.objects.create(name=name) for name in ["Family", "Work", "Friends", "Travel"]]

        # Create Contact Types
        contact_types = [ContactType.objects.create(name=name) for name in ["Phone", "Email", "Telegram", "LinkedIn", "Other"]]

        # Create Contacts
        for _ in range(20):
            contact = Contact.objects.create(name=fake.name(), birthday=fake.date_of_birth())
            contact.groups.set(random.sample(contact_groups, random.randint(1, len(contact_groups))))

            for _ in range(random.randint(1, 3)):
                contact_data = ContactData.objects.create(
                    contact=contact,
                    type=random.choice(contact_types),
                    value=fake.phone_number() if random.choice([True, False]) else fake.email()
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake contacts'))
