from django import forms
from .models import Contact, ContactGroup, ContactType


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "birthday"]


class ContactGroupForm(forms.ModelForm):
    class Meta:
        model = ContactGroup
        fields = ["name"]


class ContactTypeForm(forms.ModelForm):
    class Meta:
        model = ContactType
        fields = ["name"]
