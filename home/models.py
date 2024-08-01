from django.db import models

class Album(models.Model):
    name = models.CharField(max_length = 20)
    release_date = models.DateField()

class Clothes(models.Model):
    color = models.CharField(max_length = 20)
    size = models.SmallIntegerField()

class Product(models.Model):
    albums = models.ManyToManyField(Album, related_name = 'albums')
    clothes = models.ManyToManyField(Clothes, related_name = 'clothes')

class LIFE(models.Model):
    name = models.CharField(max_length = 50)

class Main(models.Model):
    name = models.CharField(max_length = 255)
    founded_date = models.DateField()
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    community = models.ManyToManyField(LIFE, related_name = 'LIFE')

