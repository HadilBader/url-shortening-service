from rest_framework import serializers


# TODO: document this module
class URLObjectSerializer(serializers.Serializer):
    long_version = serializers.URLField()
    short_version = serializers.URLField()
    created_at = serializers.DateTimeField()

class URLSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)

