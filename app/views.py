from django.shortcuts import render
from django.views import View
from faker import Faker
from webargs import fields, validate
from webargs.djangoparser import use_args

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

            user = {"login": login, "email": email, "password": password}

            generated_logins.add(login)
            generated_emails.add(email)
            users.append(user)

        return render(request, "user_list.html", {"users": users})
