# Generated by Django 4.2.2 on 2023-09-24 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='isAccept',
            field=models.BooleanField(default=False, verbose_name='Принял ли?'),
        ),
    ]