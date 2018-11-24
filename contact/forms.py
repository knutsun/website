from django import forms
from . import models
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ['subject', 'name', 'email', 'body']