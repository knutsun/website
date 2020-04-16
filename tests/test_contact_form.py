# from django.urls import resolve
# from django.http import HttpRequest
# from django.test import TestCase
# from django.template.loader import render_to_string
# from sermons.views import index


# class TestContactForm(TestCase):

#     def test_contact_url_resolves_to_contact_page_view(self):
#         found = resolve('/sermons')
#         print(found.func)
#         # self.assertEqual(found.func, index)

#     # def test_home_page_returns_correct_html(self):
#     #     response = self.client.get('/')
#     #     html = response.content.decode('utf8')

#     #     self.assertTrue(html.startswith('<!doctype html>\n<html lang="en">'))
#     #     self.assertIn('<title>Gateway Baptist Church</title>', html)
#     #     self.assertTrue(html.strip().endswith('</html>'))

#     # def test_home_page_uses_correct_template(self):
#     #     response = self.client.get('/')
#     #     self.assertTemplateUsed(response, 'index.html')
