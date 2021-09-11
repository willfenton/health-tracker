from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpRequest
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


def profile(request: HttpRequest):
    if request.user.is_authenticated:
        user = TrackerUser(request.user)
        badges = user.get_badges()
        points = user.get_points()
        events = Events.objects.filter(userId=user.id).order_by('-activity_date')[:10:1]
        print(badges)
        return render(request, 'profile.html', {'badges': badges, 'points': points, 'events': events})
    else:
        return redirect('base_app:login')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('base_app:profileprofile')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")

    form = RegisterForm()
    return render(request, 'registration/register.html', context={'form': form})
