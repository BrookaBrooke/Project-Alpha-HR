from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.


def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user=user)
            return redirect("home")
        else:
            form = UserCreationForm
    return render(
        request,
        "registration/signup.html",
    )
