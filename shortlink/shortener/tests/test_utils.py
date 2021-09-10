"""
This module contains tests for utility functions and classes: encode_url()
"""
from django.test import SimpleTestCase

from shortener.utils import encode_url


class TestUtils(SimpleTestCase):
    """
    This class tests the function encode_url() from shortener.utils
    """
    def test_encode_url(self):
        """
        Ensures function encodes a url correctly given a host and the url's id
        """
        self.assertEqual(encode_url('http://localhost:8000/', 35), 'http://localhost:8000/Z')
