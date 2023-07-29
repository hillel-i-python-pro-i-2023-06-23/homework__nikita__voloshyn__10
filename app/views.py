from django.shortcuts import render
from .models import Contact


def home(request):
    return render(request, "home.html")


def contact_list(request):
    # Получаем список всех контактов из базы данных
    contacts = Contact.objects.all()

    # Создаем контекст данных, которые будут переданы в шаблон
    context = {
        "contacts": contacts,
    }

    # Возвращаем ответ с отрисованным шаблоном contact_list.html и переданным контекстом
    return render(request, "contact_list.html", context)
