from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('base_app:index')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")

    form = RegisterForm()
    return render(request, 'registration/register.html', context={'form': form})
