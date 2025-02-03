from rest_framework import serializers  
from .models import  ImageStorage

class ImageStorageSerializer(serializers.ModelSerializer):
    class Meta:  
        model = ImageStorage  
        fields = ('id', 'image_id', 'published')