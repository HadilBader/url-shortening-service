from django.urls import path, re_path
from shortener.views import *

# TODO: document this module
urlpatterns = [
    path('encode', encode, name='encode'),
    path('decode', decode, name='decode'),
    re_path(r'(?P<url_id>[0-9A-Z]{1,8})', redirect_url, name='redirect')
]
