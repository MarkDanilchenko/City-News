from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from . import forms, models


# registration
def registration(request):
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            userLogIn = authenticate(username=username, password=password)
            login(request, userLogIn)
            return redirect("/")
    else:
        form = forms.UserForm()
    return render(request, "registration.html", {"form": form})
