from django.contrib import admin
from .models import Contact, ContactGroup, ContactType, ContactData

class ContactDataInline(admin.TabularInline):
    model = ContactData

class ContactAdmin(admin.ModelAdmin):
    inlines = [ContactDataInline]

admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactGroup)
admin.site.register(ContactType)
admin.site.register(ContactData)
