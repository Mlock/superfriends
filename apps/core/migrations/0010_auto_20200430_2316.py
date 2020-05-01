# Generated by Django 3.0.5 on 2020-04-30 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_delete_individualcontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
