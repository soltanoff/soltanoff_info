# Generated by Django 2.0.2 on 2018-05-04 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0006_auto_20180416_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='file',
            field=models.FileField(upload_to='storage/', verbose_name='Source'),
        ),
    ]
