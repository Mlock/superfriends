from django import forms
from datetime import datetime
from django.core.validators import validate_email
import re
from .models import Contact


EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'type', 'frequency', 'picture', 'email', 'notes', 'phone', 'address', 'birthday', 'website', 'linkedin', 'facebook',  'instagram', 'twitter',  'github',]
    notes = forms.CharField(widget=forms.Textarea, required=False)

    def clean_email(self):
            email = self.cleaned_data.get('email')

            if email and not re.match(EMAIL_REGEX, email):
                raise forms.ValidationError('Invalid email format')

            return email
            
class EditContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'type', 'frequency', 'picture', 'email', 'notes', 'phone', 'address', 'birthday', 'website', 'linkedin', 'facebook',  'instagram', 'twitter', 'github',]
    notes = forms.CharField(widget=forms.Textarea, required=False)