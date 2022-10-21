from django.db import models



class Nombres(models.Model):

    nombre = models.CharField( max_length=50)
    Dni = models.IntegerField()
    nacimiento = models.IntegerField()
