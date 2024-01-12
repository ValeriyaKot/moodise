from rest_framework import serializers
from .models import Picture, Board


class PictureSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(required=False)

    class Meta:
        model = Picture
        fields = "__all__"


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ["name", "images"]


class AddPicInSerializer(serializers.Serializer):
    board = serializers.IntegerField()
    picture = serializers.IntegerField()
