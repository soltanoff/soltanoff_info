# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 23:15
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Download count'),
        ),
    ]
