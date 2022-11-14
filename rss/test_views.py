from http import HTTPStatus
from django.test import TestCase

class RobotsTest(TestCase):
    def test_get(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response['Content-Type'], 'text_plain')
        lines = response.content.decode().splitlines()
        self.assertEqual(lines[0], 'User-Agent: *')

    def post_not_allowed(self):
        response = self.client.post('/robots.txt')
        self.assertEqual(HTTPStatus.METHOD_NOT_ALLOWED, response.status_code)
