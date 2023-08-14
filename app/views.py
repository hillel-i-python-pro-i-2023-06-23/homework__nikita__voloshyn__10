from django.shortcuts import render
from django.views import View
from faker import Faker
from webargs import fields, validate
from webargs.djangoparser import use_args
from .models import User

fake = Faker()

class UserGeneratorView(View):
    @use_args(
        {
            "count": fields.Int(required=False, missing=10, validate=validate.Range(min=1, max=100)),
        },
        location="query"
    )
    def get(self, request, args):
        users = []
        generated_logins = set()
        generated_emails = set()

        while len(users) < args["count"]:
            login = fake.user_name()
            email = fake.email()
            password = fake.password()

            if (
                not User.objects.filter(login=login).exists()
                and login not in generated_logins
                and not User.objects.filter(email=email).exists()
                and email not in generated_emails
            ):
                generated_logins.add(login)
                generated_emails.add(email)
                users.append({"login": login, "email": email, "password": password})

        return render(request, "user_list.html", {"users": users})
