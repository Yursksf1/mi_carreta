from django.core.serializers import serialize
from myapp.models import HistoryWeather
from rest_framework import serializers


class HistoryWeatherSerialize(serializers.ModelSerializer):
    class Meta:
        model = HistoryWeather
        fields = ['id',  'location', 'humidity', 'temperature', 'create_at']

    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
