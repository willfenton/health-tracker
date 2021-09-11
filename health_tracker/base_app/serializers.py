from rest_framework import serializers

from .models import Events, TrackerUser

class TrackerUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrackerUser
        fields = ('id', 'username', 'password')

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('userId', 'activity_date', 'activity', 'points')