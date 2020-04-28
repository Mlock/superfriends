# Generated by Django 3.0.5 on 2020-04-27 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30, unique=True)),
                ('last_name', models.CharField(default='', max_length=30, unique=True)),
                ('email', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default='', max_length=30)),
                ('address', models.CharField(default='', max_length=300)),
                ('birthday', models.DateField(auto_now=True)),
                ('notes', models.CharField(default='', max_length=500)),
                ('type', models.CharField(max_length=64)),
                ('frequency', models.CharField(default='', max_length=64)),
                ('votes', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('creator_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IndividualContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Contact')),
            ],
        ),
    ]
