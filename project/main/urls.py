from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view()),
    path('auth/', views.AuthPage.as_view(), name="authPage"),
    path('profile/', views.ProfilePage.as_view(), name="profilePage"),
]