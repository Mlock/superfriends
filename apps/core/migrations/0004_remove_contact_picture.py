# Generated by Django 3.0.5 on 2020-04-29 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200428_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='picture',
        ),
    ]
