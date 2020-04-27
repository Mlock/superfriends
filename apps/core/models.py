from django.db import models
from datetime import datetime

from apps.accounts.models import User

class Contact(models.Model):
    name = models.CharField(unique=True, max_length=30)
    email = models.CharField(default='', max_length=30)
    phone = models.CharField(default='', max_length=30)
    address = models.CharField(max_length=300, default='', )
    birthday = models.DateField(auto_now=True)
    notes = models.CharField(max_length=500, default='', )
    type = models.CharField(max_length=64)
    frequency = models.CharField(max_length=64, default='')
    votes = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True) # Add current date
    last_modified = models.DateTimeField(auto_now=True)

    # SOLUTION:
    creator_user = models.ForeignKey(User, on_delete=models.CASCADE)

    # BONUS SOLUTION:
    users_who_voted = models.ManyToManyField(
        User,
        related_name='friend_lists_voted_on',
    )


class Friend(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    cover_url = models.URLField(max_length=127)

    # SOLUTION:
    friend_list = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
    )

