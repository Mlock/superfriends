from django.db import models
from datetime import datetime
from apps.accounts.models import User

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='./images/', blank=True, null=True, default='/media/images/default.png')
    email = models.EmailField(blank=True, null=True, unique=True)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    birthday = models.DateField(blank=True, null=True, auto_now=False)
    notes = models.CharField(max_length=500)
    type = models.CharField(max_length=64)
    frequency = models.CharField(max_length=64)
    linkedin = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()
    created = models.DateTimeField(auto_now_add=True) # Add current date
    last_modified = models.DateTimeField(auto_now=True)

    creator_user = models.ForeignKey(User, on_delete=models.CASCADE)


class IndividualContact(models.Model):
    contact_list = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
    )

