from django.test import TestCase


class TestHome(TestCase):

    def test_sermons_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
