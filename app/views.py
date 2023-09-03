from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Contact

class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contacts'

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'view_contact.html'
    context_object_name = 'contact'

class ContactCreateView(CreateView):
    model = Contact
    template_name = 'create_contact.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('contact_list')

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'update_contact.html'
    fields = ['name', 'email']
    context_object_name = 'contact'
    success_url = reverse_lazy('contact_list')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'delete_contact.html'
    context_object_name = 'contact'
    success_url = reverse_lazy('contact_list')
