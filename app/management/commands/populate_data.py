from django.core.management.base import BaseCommand
from app.models import Contact, ContactData, ContactType
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        # Проверяем, есть ли данные в таблице Contact
        if Contact.objects.exists():
            self.stdout.write(self.style.SUCCESS('Data already exists. Skipping data population.'))
            return

        fake = Faker()

        # Создаем несколько ContactType
        contact_types = [ContactType.objects.create(name=name) for name in ["Phone", "Email", "Telegram", "LinkedIn", "Other"]]

        # Создаем несколько Contact
        for _ in range(10):
            contact = Contact.objects.create(
                name=fake.name(),
                birthday=fake.date_of_birth(minimum_age=18, maximum_age=65, tzinfo=None),
            )

            # Добавляем случайное количество ContactType к каждому Contact
            contact.types.set(random.sample(contact_types, random.randint(1, len(contact_types))))

            # Создаем несколько ContactData для каждого Contact
            for _ in range(random.randint(1, 5)):
                contact_data = ContactData.objects.create(
                    contact=contact,
                    type=random.choice(["phone", "email", "telegram", "linkedin", "other"]),
                    value=fake.phone_number() if random.choice([True, False]) else fake.email(),
                )

        self.stdout.write(self.style.SUCCESS('Data populated successfully.'))
