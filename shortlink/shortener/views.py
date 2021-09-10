"""
This module contains all views for the shortener app: encode, decode, redirect
"""
from django.http import JsonResponse
from django.shortcuts import redirect
from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework import status

from shortener.models import URL
from shortener.serializers import URLObjectSerializer, ShortURLSerializer, LongURLSerializer
from shortener.utils import encode_url


# TODO: consider moving "urls" from views to a different file
urls_dict = {}


# TODO: consider psutil to track how much memory the server is using
@api_view(['POST'])
def encode(request):
    """
    """
    serializer = LongURLSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        short_version = encode_url(request.build_absolute_uri('/'), URL.id)
        long_version = serializer.validated_data['url']
        url = URL(long_version=long_version, short_version=short_version)
        urls_dict[short_version] = url
        serializer = URLObjectSerializer(url)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(status=Http404)


# TODO: consider returning status code 422 (instead of 400)
#  if client does not send required parameter
# TODO: consider supporting url parameters, although it would
#  be awkward since the parameter itself is a url
# TODO: consider supporting POST method for decoding
@api_view(['GET'])
def decode(request):
    """
    """
    try:
        serializer = ShortURLSerializer(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            short_version = serializer.validated_data['url']
            url = urls_dict[short_version]
            serializer = URLObjectSerializer(url)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(status=Http404)
    except KeyError:
        return JsonResponse({'url': 'Are you sure you encoded this URL?'},
                            status=status.HTTP_404_NOT_FOUND)


def redirect_url(request, **kwargs):
    """
    """
    try:
        url = urls_dict[request.build_absolute_uri()].long_version
        return redirect(url)
    except KeyError:
        raise Http404("No match found for this URL")
