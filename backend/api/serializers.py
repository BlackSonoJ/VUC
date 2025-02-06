from rest_framework import serializers
from .models import Images, Events, ImagesMainPage


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ("id", "image", "published")


class ImagesMainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesMainPage
        fields = ("id", "image", "published")


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("id", "name", "description", "published")
