from rest_framework import serializers

import shortener.views as views


#TODO: document this module
class URLObjectSerializer(serializers.Serializer):
    """
    """
    long_version = serializers.URLField()
    short_version = serializers.URLField()
    created_at = serializers.DateTimeField()


class LongURLSerializer(serializers.Serializer):
    """
    """
    url = serializers.URLField(required=True)

    def validate_url(self, url):
        if len(url) <= 30:
            raise serializers.ValidationError('This URL is pretty short! Why shorten it?')
        elif url in [url.long_version for url in views.urls_dict.values()]:
            raise serializers.ValidationError('This URL already exists in the system!')
        return url

    def validate(self, attrs):
        if len(views.urls_dict) == int('ZZZZZZZZ', 36):
            raise serializers.ValidationError('Sorry! I cannot encode this URL. I am full!')
        return attrs


class ShortURLSerializer(serializers.Serializer):
    """
    """
    url = serializers.URLField(required=True, max_length=30)

