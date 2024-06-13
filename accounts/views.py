from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


def return_partial_or_full(request, partial_template, full_template):
    if request.htmx:
        template_name = partial_template
    else:
        template_name = full_template

    return template_name

def home(request):
    template_name = return_partial_or_full(
        request, "accounts_home.html", "full/accounts_home_full.html"
    )
    return render(request, template_name, {})
