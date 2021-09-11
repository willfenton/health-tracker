from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import UserCreationForm


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # match credentials to user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # log user in
            return redirect('profile')  # redirect to profile - get name/url of page to redirect to
        else:
            message.error(request, 'Username OR Password is incorrect')

    return render(request, 'login.html')  # failure to log in


def register(request):
    if request.method == 'POST':
        # create user
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # login and authenticate user
            return redirect('login')  # redirect to profile - get name/url of page to redirect to

    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')  # redirect to profile - get name/url of page to redirect to
