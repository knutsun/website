from .forms import ContactForm
import unittest

from enums.error_messages import ErrorMessages


class TestContactForm(unittest.TestCase):

    def test_form_validation_for_blank_items(self):
        form = ContactForm(data={'subject': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['subject'],
                                    [ErrorMessages.EMPTY_SUBJECT])
