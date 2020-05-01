from django.db import models
from datetime import datetime
from apps.accounts.models import User

import hashlib

FREQUENCY = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', "Monthly"),
    ('quarterly', "Quarterly"),
    ('yearly', "Yearly"),
    ('custom', "Custom"),
]

RELATION = [
    ('friend', 'Friend'),
    ('business', 'Business Contact'),
    ('volunteer', "Volunteer"),
    ('student', "Student"),
    ('custom', "Custom"),
]

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='./images/', blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True, auto_now=False)
    notes = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=64, choices=RELATION)
    frequency = models.CharField(max_length=64, choices=FREQUENCY)

    # new version

    # need to update form input for the below
    # frequency = models.IntegerField(choices=FREQUENCY)

    # this updates only if save is clicked AND frequency has been updated
    # frequency_modified = models.DurationField()

    # snooze should not affect the due date, only hide it from the displayed list
    # so it needs to be a separate value
    # snooze = models.DateTimeField() # Add current date to the number of times pushed?

    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True) # Add current date
    last_modified = models.DateTimeField(auto_now=True)

    creator_user = models.ForeignKey(User, on_delete=models.CASCADE)


# class IndividualContact(models.Model):
#     contact_list = models.ForeignKey(
#         Contact,
#         on_delete=models.CASCADE,
#     )

