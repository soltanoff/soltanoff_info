# Generated by Django 2.0.3 on 2018-03-30 16:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180315_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=100000),
        ),
    ]
