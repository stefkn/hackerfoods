from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib import auth
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def return_partial_or_full(request, partial_template, full_template):
    if request.htmx:
        template_name = partial_template
    else:
        template_name = full_template

    return template_name

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        template_name = return_partial_or_full(
            request, "signup.html", "full/signup_full.html"
        )
        return render(request, template_name, {"form": self.form_class})

def home(request):
    template_name = return_partial_or_full(
        request, "accounts_home.html", "full/accounts_home_full.html"
    )
    return render(request, template_name, {})

def login(request):
    template_name = return_partial_or_full(
        request, "login.html", "full/login_full.html"
    )

    if request.method != "POST":
        return render(request, template_name, {"form": AuthenticationForm()})

    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(request, username=username, password=password)

    if user is not None:
        auth.login(request, user)
    else:
        return render(request, template_name, {"error": "Invalid credentials"})
    
    template_name = return_partial_or_full(
        request, "accounts_home.html", "full/accounts_home_full.html"
    )

    return render(request, template_name, {})

def logout(request):
    auth.logout(request)
    template_name = return_partial_or_full(
        request, "accounts_home.html", "full/accounts_home_full.html"
    )
    return render(request, template_name, {})