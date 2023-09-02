from django.contrib import admin
from .models import Contact, ContactGroup, ContactType

admin.site.register(Contact)
admin.site.register(ContactGroup)
admin.site.register(ContactType)
