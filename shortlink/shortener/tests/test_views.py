"""
This module contains tests for the API endpoints: /encode, /decode, /
"""
import os
import json
from random import choice

from django.test import TestCase
from django.urls import reverse
from django.test.client import Client

from shortener import views
from shortener.models import URL


class CustomClient(Client):
    """
    Needed to create a custom client to change the name of the default test server
    (http://testserver/) to a name that would be validated by URLSerializer
    """
    def _base_environ(self, **request):
        """
        Changes default name of test server to localhost:8000
        """
        base = super()._base_environ(**request)
        base['SERVER_NAME'] = 'localhost:8000'
        return base


class TestViews(TestCase):
    """
    TestCase for view
    """
    def setUp(self):
        """
        Randomly chooses a long URL from the file long_urls.txt in
        the project's directory and then sends a post request to
        the server to encode the URL into a shorter one before every test
        """
        self.client = CustomClient()
        test_file_path = f'{os.getcwd()}\\long_urls.txt'
        with open(test_file_path, encoding="utf-8") as test_file:
            lines = test_file.readlines()
            self.urls = [line.rstrip() for line in lines]
        self.initial_url = choice(self.urls)
        # print(self.initial_url)
        self.response = self.client.post(reverse('encode'), {'url': self.initial_url})
        self.response_body = json.loads(self.response.content)

    def tearDown(self):
        """
        Resets URL counter/id and clears the content of url_dict after every
        test, which the in-memory data structure in which all URL objects are held
        """
        views.urls_dict = {}
        URL.id = 0

    def test_encode(self):
        """
        Ensures that the server sends a 201 response status along with an
        appropriate response body if the client sends a correct POST request
        """
        self.assertEqual(self.response.status_code, 201)
        self.assertEqual(self.response_body['long_version'], self.initial_url)

    def test_encode_no_url(self):
        """
        Ensures that server sends a 400 response in case the client does
        not send the url in the POST body
        """
        response = self.client.post(reverse('encode'))
        self.assertEqual(response.status_code, 400)

    def test_encode_duplicate_url(self):
        """
        Ensures that server sends a 400 response in case the client sends
        a url that does already exist in the server
        """
        response = self.client.post(reverse('encode'), {'url': self.initial_url})
        self.assertEqual(response.status_code, 400)

# TODO: figure out why 'http://testserver/ is not a valid URL
    def test_decode(self):
        """
        Ensures the client gets a 200 response with appropriate
        response body when a correct get request is sent
        """
        get_response = self.client.get(reverse('decode'),
                                       {'url': self.response_body['short_version']})
        self.assertEqual(get_response.status_code, 200)
        correct_url_object = views.urls_dict[self.response_body['short_version']]
        correct_response_data = {
            'long_version': correct_url_object.long_version,
            'short_version': correct_url_object.short_version,
            'created_at': str(correct_url_object.created_at)
        }
        self.assertEqual(json.loads(get_response.content), correct_response_data)

    def test_decode_no_url(self):
        """
        Ensures an appropriate response and status codes have been
        sent in case the client does not send the url as a query parameter
        """
        response = self.client.get(reverse('decode'))
        self.assertEqual(response.status_code, 400)

    def test_decode_non_existing_url(self):
        """
        Ensures an appropriate response and status codes have been
        sent in case the client requesting the decoding of a url
        that does not exist in the system
        """
        response = self.client.get(reverse('decode'), {'url': 'http://localhost:8000/1'})
        self.assertEqual(response.status_code, 404)

    def test_redirect_url(self):
        """
        Ensures that view_redirect redirects correctly
        """
        self.assertEqual(self.response.status_code, 201)
        get_response = self.client.get(self.response_body['short_version'])
        # print("Response body", self.response_body)
        self.assertEqual(get_response.status_code, 302)
        self.assertEqual(get_response.url, self.response_body['long_version'])

    def test_redirect_url_non_existing_url(self):
        """
        Ensures a 404 response status is sent to the client
        in case the client requests a url that does not have a match
        """
        get_response = self.client.get('http://localhost:8000/1')
        self.assertEqual(get_response.status_code, 404)
