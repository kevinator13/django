from django.db import models

# Create your models here.
class App(models.Model):
    name = models.CharField(max_length = 50)
    paradigm = models.CharField(max_length = 50)
