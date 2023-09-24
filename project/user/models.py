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


class Project(models.Model):
    nameProject = models.CharField('Назваение проекта', max_length=200)
    waitSolary = models.CharField('Ожидаемая оплата', max_length=200)
    description = models.CharField('Описание проекта', max_length=300)
    list_skill = models.CharField('Перечень требуемых навыков', max_length=200)
    list_task = models.CharField('Перечень требуемых задач', max_length=200)

    posts = models.CharField('Необходимые должности', max_length=1000) 

    user = models.ForeignKey('CustomUser', related_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Notification(models.Model):
    message = models.CharField('Краткая информация', max_length=200)
    number_phone = models.CharField('Номер телефона', max_length=20)
    state = models.CharField('Состояние', default='Active', max_length=50)
    isAccept = models.BooleanField('Принял ли?', default=True)
    recipient = models.ForeignKey('CustomUser', related_name='RecipientUser', on_delete=models.CASCADE)
    sender = models.ForeignKey('CustomUser', related_name='SenderUser', on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.recipient}'

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

