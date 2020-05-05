from django.forms import ModelForm

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
