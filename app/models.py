from django.db import models
from django.contrib.auth.models import User


class ContactGroup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ContactType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField(ContactGroup, blank=True)
    types = models.ManyToManyField(ContactType, blank=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    telegram = models.CharField(max_length=255, blank=True)
    linkedin = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class ContactData(models.Model):
    CONTACT_DATA_TYPES = (
        ("phone", "Phone"),
        ("email", "Email"),
        ("telegram", "Telegram"),
        ("linkedin", "LinkedIn"),
        ("other", "Other"),
    )

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=CONTACT_DATA_TYPES)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.get_type_display()}: {self.value}"
