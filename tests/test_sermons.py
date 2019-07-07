from django.test import TestCase
from django.core.files import File
from django.db import models

from unittest.mock import MagicMock
import datetime
import six
import pdb


class TestHome(TestCase):

    def test_sermon_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_can_create_sermon(self):

        data = {
            'title': 'Test',
            'date': datetime.date(2019, 2, 1),
            'description': 'Description',
            'file': MagicMock(spec=File)

        }
        response = self.client.post('/api/sermons/', data=data)
        self.assertEqual(response.status_code, 201)

