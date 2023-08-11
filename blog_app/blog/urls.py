from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login-page'),
    path('signup/', views.signup, name='signup-page'),
    path('home/', views.home, name='home-page'),
]
