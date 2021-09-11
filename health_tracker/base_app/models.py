from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Events(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_date = models.DateTimeField("activity date")
    activity = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
   