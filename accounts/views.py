from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login

def login_view(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST or None)
        # print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        else:
            print(form.errors)

    context = {
        "form":form
    }
    return render(request, "accounts/login.html", context)