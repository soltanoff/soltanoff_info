# Generated by Django 2.0.2 on 2018-03-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_auto_20180308_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(auto_now=True, verbose_name='Publication date'),
        ),
    ]