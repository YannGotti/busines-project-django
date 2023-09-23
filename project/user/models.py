from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    photo_profile = models.ImageField('Фото профиля пользователя', upload_to='photo_profile/', default='defaut_profile.png', blank=True, null=True)
    date_register = models.DateField('Дата регистрации', auto_now_add=True)
    email = models.EmailField('Почта пользователя', max_length=254)
    type_user = models.CharField('Тип пользователя', max_length=50)
    userPlaceOfStudy = models.CharField('Место обучения', max_length=250)
    fullName = models.CharField('ФИО пользователя', max_length=250)

class Questionnaire(models.Model):
    new_work = models.CharField('Кем хочет работать? (должность)', max_length=200)
    areaOfWork = models.CharField('В какой сфере хочет работать?', max_length=200)
    old_work = models.CharField('Кем работал? Как долго? Что выполнял?', max_length=300)
    experience = models.CharField('Есть ли опыт работы?', max_length=200)
    salary = models.IntegerField('Желаемая зарплата')
    freework = models.BooleanField('Работа ради опыта?', default=False)
    user = models.ForeignKey('CustomUser', related_name='CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'

