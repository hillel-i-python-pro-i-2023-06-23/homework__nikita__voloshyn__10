import random
from faker import Faker
from app.models import Contact, ContactGroup, ContactType, ContactData

fake = Faker()


def generate_users_function():
    # Create Contact Groups
    contact_groups = [ContactGroup.objects.create(name=name) for name in ["Family", "Work", "Friends", "Travel"]]

    # Create Contact Types
    contact_types = [
        ContactType.objects.create(name=name) for name in ["Phone", "Email", "Telegram", "LinkedIn", "Other"]
    ]

    # Create Contacts
    for _ in range(20):
        contact = Contact.objects.create(name=fake.name(), birthday=fake.date_of_birth())
        contact.groups.set(random.sample(contact_groups, random.randint(1, len(contact_groups))))

        for _ in range(random.randint(1, 3)):
            ContactData.objects.create(
                contact=contact,
                type=random.choice(contact_types),
                value=fake.phone_number() if random.choice([True, False]) else fake.email(),
            )
