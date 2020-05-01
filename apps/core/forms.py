from django import forms
from datetime import datetime
from django.core.validators import validate_email
import re
from .models import Contact


EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'picture', 'email', 'notes', 'phone', 'address', 'birthday', 'type', 'frequency', 'website', 'linkedin', 'facebook',  'instagram', 'twitter',  'github',]
    notes = forms.CharField(widget=forms.Textarea, required=False)

    def clean_email(self):
            email = self.cleaned_data.get('email')

            if email and not re.match(EMAIL_REGEX, email):
                raise forms.ValidationError('Invalid email format')

            return email
            
class EditContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'picture', 'email', 'notes', 'phone', 'address', 'birthday', 'type', 'frequency', 'website', 'linkedin', 'facebook',  'instagram', 'twitter', 'github',]
    notes = forms.CharField(widget=forms.Textarea, required=False)


# class AddFriendForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField(widget=forms.Textarea)


# class AddContactForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     picture = forms.ImageField(required=False, allow_empty_file=True)

        
#     email = forms.EmailField()

#     phone = forms.CharField(required=False)
#     address = forms.CharField(required=False)
#     birthday = forms.DateField(required=False)
#     notes = forms.CharField(widget=forms.Textarea)
#     type = forms.ChoiceField(choices=RELATION)
#     frequency = forms.ChoiceField(choices=FREQUENCY)
#     linkedin = forms.URLField(required=False)
#     facebook = forms.URLField(required=False)
#     instagram = forms.URLField(required=False)
#     twitter = forms.URLField(required=False)

