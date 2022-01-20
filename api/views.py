from django.shortcuts import render
from api.models import Region, Fruit
from api.serializers import Regionserializer, Fruitserializer
from rest_framework import viewsets

# Create your views here.
class Regionapi(viewsets.ModelViewSet):
  queryset=Region.objects.all()
  serializer_class=Regionserializer

class Fruitapi(viewsets.ModelViewSet):
  queryset=Fruit.objects.all()
  serializer_class=Fruitserializer