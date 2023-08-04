from django.core.management.base import BaseCommand
from datetime import datetime
from app.models import Contact


class Command(BaseCommand):
    help = "Generate contacts"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, default=10, help="Number of contacts to generate.")

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        for _ in range(count):
            name = "Contact " + str(datetime.now().microsecond)
            phone = "Phone " + str(datetime.now().microsecond)
            contact = Contact.objects.create(name=name, phone=phone)
            contact.save()
