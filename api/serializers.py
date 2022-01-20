from rest_framework import serializers
from api.models import Region,Fruit



class Fruitserializer(serializers.ModelSerializer):
  class Meta:
    model=Fruit
    fields="__all__"
  
  
class Regionserializer(serializers.ModelSerializer):
  Regionid=Fruitserializer(read_only=True,many=True)
  class Meta:
    model=Region
    fields="__all__"

    
