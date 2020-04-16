from django.core.files import File
from django.test import TestCase

import datetime
import mock

from .models import Sermons


class TestSermonModel(TestCase):

    def test_saving_and_retrieving_sermons(self):

        # Arrange
        first_sermon = Sermons()
        first_sermon.title = 'Easter, the Resurrection'
        first_sermon.date = datetime.datetime(2020, 5, 17)
        first_sermon.description = 'This is a sermon on Easter'

        # Mock File object
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.mp3'
        first_sermon.file = file_mock

        # Act
        # Save Sermon to database
        first_sermon.save()

        # Retrieve Sermon from database
        saved_sermons = Sermons.objects.all()
        first_saved_sermon = saved_sermons[0]

        # Assert
        self.assertEqual(saved_sermons.count(), 1)
        self.assertEqual(first_saved_sermon.title, 'Easter, the Resurrection')
        self.assertEqual(str(first_saved_sermon.date), '2020-05-17')
        self.assertEqual(first_saved_sermon.description, 'This is a sermon on Easter')
        self.assertTrue(first_saved_sermon.file.name.startswith('test_'))
        self.assertTrue(first_saved_sermon.file.name.endswith('.mp3'))


