from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Contact
from .management.commands.populate_contacts import generate_users_function


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contact_list.html", {"contacts": contacts})


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "contact_detail.html", {"contact": contact})


def generate_users(request):
    if request.method == "POST":
        generate_users_function()

        return HttpResponseRedirect("/admin")

    return render(request, "generate_users.html")
