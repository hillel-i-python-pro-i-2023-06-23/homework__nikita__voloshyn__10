from django.core.management.base import BaseCommand
from app.models import Contact


class Command(BaseCommand):
    help = "Delete all contacts"

    def handle(self, *args, **kwargs):
        Contact.objects.all().delete()
