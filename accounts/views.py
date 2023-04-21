from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    context = {}
    return render(request, "accounts/login.html", context)