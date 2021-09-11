from django.contrib import admin

from .models import TrackerUser, Events

admin.site.register(Events)
admin.site.register(TrackerUser)
