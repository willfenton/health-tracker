from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import TrackerUser, Events
from .serializers import TrackerUserSerializer, EventsSerializer
from .forms import RegisterForm


class TrackerUserViewSet(viewsets.ModelViewSet):
    queryset = TrackerUser.objects.all().order_by('id')
    serializer_class = TrackerUserSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('userId')
    serializer_class = EventsSerializer


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
