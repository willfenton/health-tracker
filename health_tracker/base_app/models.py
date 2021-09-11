from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
import datetime

# Create your models here.
class Events(models.Model):
    userId = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    activity_date = models.DateTimeField("activity date")
    activity = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
   
class TrackerUser(User):
    class Meta:
        proxy = True

    def get_badges(self):
        point_total = self.get_points()
        badges_cutoffs = {
            "gold": 30,
            "silver": 20,
            "bronze": 10
        }
        keys = badges_cutoffs.keys()
        badges = []
        for key in keys:
            if point_total > badges_cutoffs.get(key):
                badges.append(key)

        return badges

    def get_points(self):
        user_events = Events.objects.filter()
        point_total = 0
        for event in user_events:
            point_total += event.points
        
        return point_total