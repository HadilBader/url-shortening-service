from django.test import SimpleTestCase
from shortener.utils import encode_url


class TestUtils(SimpleTestCase):

    def test_encode_url(self):
        self.assertEqual(encode_url('http://localhost:8000/', 35), 'http://localhost:8000/Z')
