from django.db import models

# Create your models here.

class editor(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    creationDate= models.IntegerField(default=0)

class manufacturer(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    creationDate = models.IntegerField(default=0)

class platform(models.Model):
    def __str__(self):
        return self.name
    PC = 'PC'
    SALON = 'SA'
    PORTABLE = 'PO'
    HYBRIDE = 'HY'
    PLATFORM_TYPE = (
        (PC, 'PC'),
        (SALON, 'Salon'),
        (PORTABLE, 'Portable'),
        (HYBRIDE,'Hybride'),
    )
    name  = models.CharField(max_length=100)
    category = models.CharField(max_length=10,choices=PLATFORM_TYPE,default=PC)
    year = models.IntegerField(default=0)
    constructor = models.ForeignKey(manufacturer,on_delete=models.PROTECT)

class videoGame(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    editor = models.ForeignKey(editor,on_delete=models.PROTECT)
    platform = models.ForeignKey(platform,on_delete=models.PROTECT)
    year = models.IntegerField(default=0)
    played = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
