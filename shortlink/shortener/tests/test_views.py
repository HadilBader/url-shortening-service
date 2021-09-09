from django.test import TestCase, Client
from django.urls import reverse
import json
import os
from random import choice


# TODO: add tests for other aspects
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        test_file_path = f'{os.getcwd()}\\long_urls.txt'
        with open(test_file_path) as test_file:
            lines = test_file.readlines()
            self.urls = [line.rstrip() for line in lines]

    def test_encode(self):
        response = self.client.post(reverse('encode'), {'url': choice(self.urls)})
        self.assertEqual(response.status_code, 201)
        print(f'Created URL object: {response.content}')

# TODO: figure out why 'http://testserver/0 is not a valid URL
    def test_decode(self):
        post_response = self.client.post(reverse('encode'), {'url': choice(self.urls)})
        data = json.loads(post_response.content)
        print(data['short_version'])
        get_response = self.client.get(reverse('decode'), {'url': data['short_version']})
        print(get_response.content)
        self.assertEqual(get_response.status_code, 200)

    def test_redirect_url(self):
        post_response = self.client.post(reverse('encode'), {'url': choice(self.urls)})
        data = json.loads(post_response.content)
        get_response = self.client.get(data['short_version'])
        self.assertEqual(get_response.status_code, 302)
