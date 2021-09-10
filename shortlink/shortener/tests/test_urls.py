"""
This module contains tests for routers in shortener.urls
"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from shortener.views import encode, decode, redirect_url


class TestUrls(SimpleTestCase):
    """
    This class contains tests for routers in shortener.urls
    """

    def test_encode_url_resolves(self):
        """
        Ensures endpoint /encode resolves correctly
        """
        url = reverse('encode')
        self.assertEqual(resolve(url).func, encode)

    def test_decode_url_resolves(self):
        """
        Ensures endpoint /decode resolves correctly
        """
        url = reverse('decode')
        self.assertEqual(resolve(url).func, decode)

    def test_redirect_url_resolves(self):
        """
        Ensures endpoint / resolves correctly
        """
        url = reverse('redirect', kwargs={'url_id': 'ID'})
        self.assertEqual(resolve(url).func, redirect_url)
