from rest_framework import serializers
from .models import Manufacturer, ShoeType, ShoeColor, Shoe

# Will show me info relevent to my model
# Meta class
# serializer will translate JSON into our model for HTTP requests


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'url')


class ShoeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('id', 'style')


class ShoeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('id', 'color_name')


class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = ('id', 'url', 'size', 'brandname', 'manufacturer',
                  'color', 'material', 'shoe_type', 'fasten_type')
