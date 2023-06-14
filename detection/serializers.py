from rest_framework import serializers
from rest_framework.serializers import ImageField, CharField


class DetectImageSer(serializers.Serializer):
    file = ImageField(allow_empty_file=False)
    text = CharField()
