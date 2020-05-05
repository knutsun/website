from .forms import ContactForm
import unittest

# from enums.error_messages import ErrorMessages

EMPTY_SUBJECT = 'Subject is invalid. Please enter a valid subject.'
EMPTY_NAME = 'Name is invalid. Please enter a valid name.'


class TestContactForm(unittest.TestCase):

    def test_form_validation_for_blank_subject(self):
        form = ContactForm(data={'subject': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['subject'],
                                    ['Subject is invalid. Please enter a valid subject.'])

    def test_form_validation_for_blank_name(self):
        form = ContactForm(data={'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'],
                                    ['Name is invalid. Please enter a valid name.'])

    def test_form_validation_for_blank_email(self):
        form = ContactForm(data={'email': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'],
                                    ['Email is invalid. Please enter a valid email.'])

    def test_form_validation_for_blank_body(self):
        form = ContactForm(data={'body': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['body'],
                                    ['Message is invalid. Please enter a valid message.'])
