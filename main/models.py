from django.db import models
from django.db.models import TextField, ImageField, Model
import datetime

class Register(models.Model):
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birth = models.DateField(default=datetime.date.today)
    phone = models.CharField(max_length=255)
    full_adress = models.CharField(max_length=255)

class Image(models.Model):
    image = models.ImageField()

class TextHome(models.Model):
    image = ImageField()
    text = TextField()

class TextFill(models.Model):
    text = models.TextField()

class IMSJ(models.Model):
    status = models.IntegerField(choices=(
        (1,"Intelektual"),
        (2,"Maxsus tayyorgarlik"),
        (3,"Shaxsiy (ruhiy, psixologik)"),
        (4,"Jismoniy"),
    ))
    image = models.ImageField()
    text = models.TextField()

class Intelekt(models.Model):
    savol_matni = models.ImageField(max_length=255)


class IntelektVariant(models.Model):
    savol = models.ForeignKey(Intelekt, related_name='variantlar', on_delete=models.CASCADE)
    matn = models.ImageField(max_length=255)
    is_correct = models.BooleanField(default=False)


class Maxsus(models.Model):
    savol_matni = models.CharField(max_length=255)

    def __str__(self):
        return self.savol_matni

class MaxsusVariant(models.Model):
    savol = models.ForeignKey(Maxsus, related_name='variantlar', on_delete=models.CASCADE)
    matn = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.savol.savol_matni} - {self.matn}"

    