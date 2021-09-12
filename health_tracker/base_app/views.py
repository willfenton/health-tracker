from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from rest_framework import viewsets

from .forms import RegisterForm
from .models import TrackerUser, Events
from .serializers import TrackerUserSerializer, EventsSerializer


class TrackerUserViewSet(viewsets.ModelViewSet):
    queryset = TrackerUser.objects.all().order_by('id')
    serializer_class = TrackerUserSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('userId')
    serializer_class = EventsSerializer


class TrackerUserViewSet(viewsets.ModelViewSet):
    queryset = TrackerUser.objects.all().order_by('id')
    serializer_class = TrackerUserSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('userId')
    serializer_class = EventsSerializer


def about(request: HttpRequest):
    return render(request, 'about.html')


def my_profile(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('base_app:user_profile', username=request.user.username)
    else:
        return redirect('base_app:login')


def user_profile(request: HttpRequest, username):
    try:
        user = User.objects.get(username=username)
        return render(request, 'profile.html', {'profile_user': user})
    except:
        raise Http404()


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('base_app:my_profile')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")

    form = RegisterForm()
    return render(request, 'registration/register.html', context={'form': form})
