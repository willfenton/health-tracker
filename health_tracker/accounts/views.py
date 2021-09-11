from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # match credentials to user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)   # log user in
            return redirect('profile')  # redirect to profile - get name/url of page to redirect to
        else:
            message.error(request, 'Username OR Password is incorrect') 

    return render(request, 'accounts/login.html')   # failure to log in

def register(request):
    if request.method == 'POST':
        # create user
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()  
            
            # login and authenticate user
            return redirect('login')        # redirect to profile - get name/url of page to redirect to 

    else:
        form = CreateUserForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')        # redirect to profile - get name/url of page to redirect to 