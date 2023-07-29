# app/views.py
from django.shortcuts import render
from .models import Contact
from faker import Faker


def home(request):
    return render(request, "home.html")


def contact_list(request):
    # Проверяем, есть ли уже контакты в базе данных
    if Contact.objects.count() == 0:
        # Если нет, то создаем несколько контактов с помощью Faker
        fake = Faker()
        for _ in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            Contact.objects.create(first_name=first_name, last_name=last_name, email=email)

    # Извлекаем все объекты из модели Contact
    contacts = Contact.objects.all()

    # Передаем список контактов в шаблон и отображаем его на странице
    return render(request, "contact_list.html", {"contacts": contacts})
