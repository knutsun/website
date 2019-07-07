from django.test import TestCase
from django.core.files import File
from django.db import models
from sermons.models import Sermons

from unittest.mock import MagicMock
import datetime
import six
import pdb


class TestHome(TestCase):

    def test_sermon_page_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_can_create_sermon(self):
        description = 'Sunday\'s Sermon'
        data = {
            'title': 'Test',
            'date': datetime.date(2019, 2, 1),
            'description': description,
            'file': MagicMock(spec=File)

        }
        post_response = self.client.post('/api/sermons/', data=data)
        self.assertEqual(post_response.status_code, 201)
        self.assertIn(description, post_response.content.decode())

        sermons_response = self.client.get('/api/sermons/')
        self.assertContains(sermons_response, description)

