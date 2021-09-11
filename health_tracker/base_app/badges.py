from django.contrib.auth.models import User
from .models import Events


def get_badges(self):
    point_total = self.get_points()
    badges_cutoffs = {
        "gold": 30,
        "silver": 20,
        "branze": 10
    }
    keys = badges_cutoffs.keys()
    badges = []
    for key in keys:
        if point_total > badges_cutoffs.get(key):
            badges.append(key)

    return badges

def get_points(self):
    user_events = Events.objects.filter(username = self.username)
    point_total = 0
    for event in user_events:
        point_total += event.points
    
    return point_total

User.add_to_class("get_badges", get_badges)
User.add_to_class("get_points", get_points)