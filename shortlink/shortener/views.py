from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from shortener.models import URL
from rest_framework import status
from shortener.serializers import URLObjectSerializer, URLSerializer
from shortener.utils import encode_url

# TODO: consider class-based views
# TODO: consider defining error JSON responses once
# TODO: consider moving "urls" from views to a different file
# TODO: document this module
urls = {}


@api_view(['POST'])
def encode(request):
    serializer = URLSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        short_version = encode_url(request.build_absolute_uri('/'), URL.id)
        long_version = serializer.validated_data['url']
        url = URL(long_version=long_version, short_version=short_version)
        urls[short_version] = url
        serializer = URLObjectSerializer(url)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


# TODO: consider returning status code 422 (instead of 400) if client does not send required parameter
# TODO: consider supporting url parameters, although it would be awkward since the parameter itself is a url
# TODO: consider supporting POST method for decoding
@api_view(['GET'])
def decode(request):
    try:
        serializer = URLSerializer(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            short_version = serializer.validated_data['url']
            url = urls[short_version]
            serializer = URLObjectSerializer(url)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    except KeyError:
        return JsonResponse({'error': 'No original url found for this encoded url'}, status=status.HTTP_404_NOT_FOUND)


def redirect_url(request, **kwargs):
    try:
        url = urls[request.build_absolute_uri()].long_version
        return redirect(url)
    except KeyError:
        return JsonResponse({'error': 'No original url found for this encoded url'}, status=status.HTTP_404_NOT_FOUND)
