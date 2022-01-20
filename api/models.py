from django.db import models

# Create your models here.
class Region(models.Model):
  regionid = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=100)


class Fruit(models.Model):
  name = models.CharField(max_length=100) 
  regionid = models.ForeignKey(Region,related_name='Regionid',on_delete=models.CASCADE)

  
