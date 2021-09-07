from rest_framework import serializers
from shortener.models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['long_version', 'short_version', 'created_at']

