# Generated by Django 3.0.5 on 2020-04-27 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='users_who_voted',
        ),
    ]
