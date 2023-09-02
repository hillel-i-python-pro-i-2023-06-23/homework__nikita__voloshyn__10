from django.db import models

class ContactGroup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ContactType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    groups = models.ManyToManyField(ContactGroup)
    types = models.ManyToManyField(ContactType)

    def __str__(self):
        return self.name

class ContactData(models.Model):
    CONTACT_DATA_TYPES = (
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('telegram', 'Telegram'),
        ('linkedin', 'LinkedIn'),
        ('other', 'Other'),
    )

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=CONTACT_DATA_TYPES)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.get_type_display()}: {self.value}"

class ContactGroupMembership(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    group = models.ForeignKey(ContactGroup, on_delete=models.CASCADE)

class ContactTypeMembership(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    type = models.ForeignKey(ContactType, on_delete=models.CASCADE)
