# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 23:25
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_filemodel_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='file',
            field=models.FileField(upload_to=b'', verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='file_name',
            field=models.CharField(max_length=20, verbose_name='Title'),
        ),
    ]
