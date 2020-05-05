from django.forms import ModelForm

from enums.error_messages import ErrorMessages
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'name', 'email', 'body']

        error_messages = {
            'subject': {'required': ErrorMessages.EMPTY_SUBJECT}
        }
