"""
This module is response for routing
"""
from django.urls import path, re_path
from shortener.views import encode, decode, redirect_url


urlpatterns = [
    path('encode', encode, name='encode'),
    path('decode', decode, name='decode'),
    re_path(r'(?P<url_id>[0-9A-Z]{1,8})', redirect_url, name='redirect')
]
