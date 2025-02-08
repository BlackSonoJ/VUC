from rest_framework import serializers
from .models import Images, Events, ImagesMainPage, Videos


class ImagesSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        image = validated_data.get("image")
        user = validated_data.get("user")
        return Images.objects.create(image=image, user=user)

    class Meta:
        model = Images
        fields = ("id", "user", "image", "published")


class ImagesMainPageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        image = validated_data.get("image")
        user = validated_data.get("user")
        return ImagesMainPage.objects.create(image=image, user=user)

    class Meta:
        model = ImagesMainPage
        fields = ("id", "user", "image", "published")


class EventsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        name = validated_data.get("name")
        user = validated_data.get("user")
        description = validated_data.get("description")
        published = validated_data.get("published")
        return Events.objects.create(
            name=name,
            user=user,
            description=description,
            published=published,
        )

    class Meta:
        model = Events
        fields = ("id", "user", "name", "description", "published")


class VideosSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        video = validated_data.get("video")
        user = validated_data.get("user")
        return Videos.objects.create(video=video, user=user)

    class Meta:
        model = Videos
        fields = ("id", "user", "video", "published")
