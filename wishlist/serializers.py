from rest_framework import serializers
from .models import FavouriteItem

class FavouriteItemSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()

    def get_content_type(self, obj):
        return obj.content_type.model

    class Meta:
        model = FavouriteItem
        fields = '__all__'