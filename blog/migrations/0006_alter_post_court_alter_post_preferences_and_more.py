# Generated by Django 5.0.2 on 2024-04-01 12:42

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='court',
            field=models.CharField(choices=[('Court A', 'Court A'), ('Court B', 'Court B'), ('Court C', 'Court C')], default='Court A', max_length=20, verbose_name='Корт'),
        ),
        migrations.AlterField(
            model_name='post',
            name='preferences',
            field=models.TextField(default='', verbose_name='Пожелания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='post',
            name='training_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='post',
            name='training_time',
            field=models.TimeField(default=datetime.time(0, 0), verbose_name='Время'),
        ),
    ]
