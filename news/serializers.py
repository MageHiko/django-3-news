from rest_framework import serializers
from .models import NewsThree


class NewsThreeSrializers(serializers.ModelSerializer):
    class Meta:
        model = NewsThree
        fields = ['id', 'title', 'description', 'image']