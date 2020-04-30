# Generated by Django 3.0.5 on 2020-04-29 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200429_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('friend', 'Friend'), ('business', 'Business Contact'), ('volunteer', 'Volunteer'), ('student', 'Student'), ('custom', 'Custom')], max_length=64),
        ),
    ]
