from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Questionnaire, Project, Notification


@admin.register(CustomUser)
class UserAdminPanel(UserAdmin):
    model = CustomUser
    #list_display = ('username', 'email', 'profile_image', 'date_register')
    
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Свои поля',
            {
                'fields': (
                    'photo_profile',
                    'email',
                    'date_register',
                    'type_user',
                    'fullName'
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Свои поля',
            {
                'fields': (
                    'photo_profile',
                    'type_user',
                    'fullName'
                )
            }
        )
    )
    readonly_fields=(
        'date_register',
    )
# Register your models here.

@admin.register(Questionnaire)
class QuestionnairePanel(admin.ModelAdmin):
    model = Questionnaire
    list_display = ('new_work', 'areaOfWork', 'old_work', 'experience', 'salary', 'freework', 'user')

@admin.register(Project)
class ProjectPanel(admin.ModelAdmin):
    model = Project
    list_display = ('nameProject', 'waitSolary', 'description', 'list_skill', 'list_task', 'posts', 'user')

@admin.register(Notification)
class NotificationPanel(admin.ModelAdmin):
    model = Notification
    list_display = ('message', 'number_phone', 'recipient', 'sender', 'state', 'isAccept')