from django.contrib.auth import views as auth_views
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.TrackerUserViewSet)
router.register(r'events', views.EventViewSet)

app_name = 'base_app'
urlpatterns = [
    path('', views.about, name='index'),
    path('about', views.about, name='about'),
    path('profile', views.my_profile, name='my_profile'),
    path('profile/<str:username>', views.user_profile, name='user_profile'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='base_app:login'), name='logout'),
    path('register', views.register, name='register'),
    path('delete-event', views.delete_event, name='delete_event'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
