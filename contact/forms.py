from django.forms import ModelForm
from django.forms import ValidationError
from django import forms

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'name', 'email', 'body']

        error_messages = {
            'subject': {'required': 'Subject is invalid. Please enter a valid subject.'},
            'name': {'required': 'Name is invalid. Please enter a valid name.'},
            'email': {'required': 'Email is invalid. Please enter a valid email.'},
            'body': {'required': 'Message is invalid. Please enter a valid message.'}
        }

    def clean_email(self):
        email = self.cleaned_data['email']

        if not email.endswith('@*.com'):
            print('toperror')
            raise ValidationError('Domain of email is not valid')

        return email
