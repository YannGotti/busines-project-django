# Generated by Django 4.2.2 on 2023-09-23 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_customuser_activeaccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo_profile',
            field=models.ImageField(blank=True, default='defaut_profile.png', null=True, upload_to='photo_profile/', verbose_name='Фото профиля пользователя'),
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_work', models.CharField(max_length=200, verbose_name='Кем хочет работать? (должность)')),
                ('areaOfWork', models.CharField(max_length=200, verbose_name='В какой сфере хочет работать?')),
                ('old_work', models.CharField(max_length=300, verbose_name='Кем работал? Как долго? Что выполнял?')),
                ('experience', models.CharField(max_length=200, verbose_name='Есть ли опыт работы?')),
                ('salary', models.IntegerField(verbose_name='Желаемая зарплата')),
                ('freework', models.BooleanField(default=False, verbose_name='Работа ради опыта?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustomUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Анкета',
                'verbose_name_plural': 'Анкеты',
            },
        ),
    ]