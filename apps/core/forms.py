from django import forms

class AddFriendForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)

RELATION = [
    ('friend', 'Friend'),
    ('business', 'Business Contact'),
    ('volunteer', "Volunteer"),
    ('student', "Student"),
    ('custom', "Custom"),
]

FREQUENCY = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', "Monthly"),
    ('quarterly', "Quarterly"),
    ('yearly', "Yearly"),
    ('custom', "Custom"),
]

class AddFriendListForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()
    address = forms.CharField()
    birthday = forms.CharField()
    notes = forms.CharField(widget=forms.Textarea)
    type = forms.ChoiceField(choices=RELATION)
    frequency = forms.ChoiceField(choices=FREQUENCY)

