"""
This module contains all views for the shortener app: encode, decode, redirect
"""
from django.http import JsonResponse
from django.shortcuts import redirect
from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.validators import ValidationError

from shortener.models import URL
from shortener.serializers import URLObjectSerializer, ShortURLSerializer, LongURLSerializer
from shortener.utils import encode_url

urls_dict = {}


@api_view(['POST'])
def encode(request):
    """
    /encode endpoint:
    Validates the received JSON, encodes it, and stores it in urls_dict
    """
    try:
        long_url_serializer = LongURLSerializer(data=request.data)
        long_url_serializer.is_valid(raise_exception=True)
        short_version = encode_url(request.build_absolute_uri('/'), URL.id)
        long_version = long_url_serializer.validated_data['url']
        url = URL(long_version=long_version, short_version=short_version)
        urls_dict[short_version] = url
        object_serializer = URLObjectSerializer(url)
        return JsonResponse(object_serializer.data, status=status.HTTP_201_CREATED)
    except ValidationError:
        return JsonResponse(long_url_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def decode(request):
    """
    /decode endpoint:
    Validates the received parameter, decodes it, and sends it as
    a JSON in the response's body
    """
    try:
        short_url_serializer = ShortURLSerializer(data=request.query_params)
        short_url_serializer.is_valid(raise_exception=True)
        short_version = short_url_serializer.validated_data['url']
        url = urls_dict[short_version]
        url_object_serializer = URLObjectSerializer(url)
        return JsonResponse(url_object_serializer.data, status=status.HTTP_200_OK)
    except ValidationError:
        return JsonResponse(short_url_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except KeyError:
        return JsonResponse({'url': 'Are you sure you encoded this URL?'},
                            status=status.HTTP_404_NOT_FOUND)


def redirect_url(request, **kwargs):
    """
    / endpoint:
    responsible for redirecting the client
    """
    try:
        url = urls_dict[request.build_absolute_uri()].long_version
        return redirect(url)
    except KeyError:
        raise Http404("No match found for this URL")
