from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view()),
    path('activate/account/', views.ActivateValidate.as_view()), 
]