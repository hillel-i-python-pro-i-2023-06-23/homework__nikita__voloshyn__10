from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Contact

@receiver(post_migrate)
def populate_data(sender, **kwargs):
    if not Contact.objects.exists():
        from django.core.management import call_command
        call_command('populate_data')
