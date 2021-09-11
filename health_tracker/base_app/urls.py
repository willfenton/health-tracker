from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'base_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='base_app:login'), name='logout'),
    path('register', views.register, name='register'),
]
