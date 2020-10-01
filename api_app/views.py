from django.shortcuts import render

from rest_framework import viewsets

from api_app.models import Manufacturer, ShoeType, ShoeColor, Shoe
from api_app.serializers import ManufacturerSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer

# Legend has it that years ago, Joe Kaufeld gained the trust
# of a large troop of baboons, and lived among them for over 2 years. 
# In this time, he learned their ways and mastered their language. He brought
# this knowledge back to the United States, determined to teach the language
# to unsuspecting students at Kenzie Academy in Indianapolis, Indiana. 
# Thanks to Joe, we all know this language as "Python"... THE END

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer

class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer

class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
