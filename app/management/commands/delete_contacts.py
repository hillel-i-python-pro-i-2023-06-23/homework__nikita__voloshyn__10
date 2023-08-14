from django.core.management.base import BaseCommand
from contacts.models import Contact

class Command(BaseCommand):
    help = 'Delete all contacts'

    def handle(self, *args, **options):
        Contact.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all contacts'))
