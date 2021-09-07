from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from datetime import datetime
from shortener import models
from rest_framework import status
from shortener import serializers

urls = {}


@api_view(['POST'])
def encode(request):
    long_version = request.data['url']
    short_version = "http://localhost:800/1"
    url = models.URL(long_version=long_version, short_version=short_version, created_at=datetime.now())
    serializer = serializers.URLSerializer(url)
    urls[short_version] = url
    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def decode(request):
    short_version = request.query_params['url']
    url = urls[short_version]
    serializer = serializers.URLSerializer(url)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)

