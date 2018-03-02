# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=20, verbose_name='File name')),
                ('notes', models.CharField(max_length=20, null=True, verbose_name='File notes')),
                ('upload_date', models.DateTimeField(null=True, verbose_name='Upload date')),
                ('file', models.FileField(upload_to=b'')),
            ],
        ),
    ]