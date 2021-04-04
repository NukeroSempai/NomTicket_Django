from django.db import models

# Create your models here.

class Comuna(models.Model):
    nombre = models.CharField(max_length=50)