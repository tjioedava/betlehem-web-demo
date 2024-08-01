from django.db import models

class Album(models.Model):
    name = models.CharField(max_length = 20)
    release_date = models.DateField()

    def __str__(self):
        return self.name + '(' + str(self.release_date) + ')'

class Clothes(models.Model):
    color = models.CharField(max_length = 20)
    size = models.SmallIntegerField()

    def __str__(self):
        return self.color + ' clothes'

class Product(models.Model):
    albums = models.ManyToManyField(Album, related_name = 'albums')
    clothes = models.ManyToManyField(Clothes, related_name = 'clothes')

class LIFE(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Main(models.Model):
    name = models.CharField(max_length = 255)
    founded_date = models.DateField()
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    community = models.ManyToManyField(LIFE, related_name = 'LIFE')

    def __str__(self):
        return self.name

