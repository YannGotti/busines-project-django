from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view()),
    path('auth/', views.AuthPage.as_view(), name="authPage"),
    path('profile/', views.ProfilePage.as_view(), name="profilePage"),
    path('@id<str:pk>/', views.ProfileUserPage.as_view()),
    path('profile/sendQuestionnaire/', views.SendQuestionnaire.as_view()),
    path('profile/publicProject/', views.PublicProject.as_view()),
    path('profile/uploadPhoto/', views.UploadPhotoProfile.as_view()),
    path('questionnaires/', views.QuestionnairesPage.as_view(), name="questionnairesPage"),
    path('questionnaires/filter/', views.QuestionnairesFilter.as_view()),
    path('projects/', views.ProjectsPage.as_view(), name="projectsPage"),

]