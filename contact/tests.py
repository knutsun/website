from django.core.files import File
from django.test import TestCase

import datetime
import mock

from .models import Contact



class TestContactPage(TestCase):

    def test_contact_page_template(self):
        response = self.client.get('/contact/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/index.html')

    def test_can_create_submission(self):

        data = {
            'subject': 'Contact subject',
            'date': datetime.date(2019, 2, 1),
            'body': 'This is the body',
            'name': 'Chaz',
            'email': 'csselph@gmail.com'

        }
        post_response = self.client.post('/contact/', data=data)
        self.assertEqual(post_response.status_code, 200)
        self.assertIn('Message successfully sent', post_response.content.decode())
