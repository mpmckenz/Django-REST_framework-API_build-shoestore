from django.shortcuts import render
from rest_framework import viewsets
from .models import Manufacturer, ShoeType, ShoeColor, Shoe
from .serializers import ManufacturerSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer

"""
1. ModelViewSets handles request methods in a general sense instead of having to define each type of request like 
this is what I want to happen when its a GET request, POST request, etc
2. those are pre- standard methods in a REST API that are constant
3. this ModelViewSet takes care of that so don't have to specify explicity
"""
"""
We only need to deal with how to get objects from db and the serializer class that is going to be used for the db

"""


class ManufacturerView(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ShoeTypeView(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeColorView(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeView(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
