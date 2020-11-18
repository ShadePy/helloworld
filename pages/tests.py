from django.http import response
from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_aboutpage_status_code(self):
        response = self.client.get('/about/') # important to write both parentheses
        self.assertEqual(response.status_code, 200)
