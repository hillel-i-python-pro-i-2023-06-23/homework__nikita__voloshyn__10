from django import forms
from .models import Contact, ContactData

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactDataForm(forms.ModelForm):
    class Meta:
        model = ContactData
        fields = '__all__'
