from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contact_list.html", {"contacts": contacts})


def create_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm()
    return render(request, "contact_form.html", {"form": form})


def view_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "contact_detail.html", {"contact": contact})


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm(instance=contact)
    return render(request, "contact_form.html", {"form": form})


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contact_list")
    return render(request, "contact_confirm_delete.html", {"contact": contact})
