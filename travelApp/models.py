from django.db import models
from datetime import date


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='picture', default=False)
    offer = models.BooleanField(default=False)


class News(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField()
    day = models.DateField(default=date.today())
    image = models.ImageField(upload_to='picture', default=False)
    category = models.CharField(max_length=250)
