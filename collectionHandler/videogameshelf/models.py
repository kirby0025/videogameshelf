from django.db import models

# Create your models here.

class editor(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    creationDate= models.IntegerField(default=0)

class videoGame(models.Model):
    title = models.CharField(max_length=200)
    editor = models.ForeignKey(editor,on_delete=models.PROTECT)
    platform = models.CharField(max_length=200)
    played = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
