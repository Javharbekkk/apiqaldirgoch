from django.db import models
import datetime


class Register(models.Model):
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birth = models.DateField(default=datetime.date.today)
    phone = models.CharField(max_length=255)
    full_adress = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.surname} {self.name} ({self.city})"


class Image(models.Model):
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"Image {self.id}"


class TextHome(models.Model):
    image = models.ImageField(upload_to="home_images/")
    text = models.TextField()

    def __str__(self):
        return f"TextHome {self.id}"


class TextFill(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"TextFill {self.id}"


class IMSJ(models.Model):
    STATUS_CHOICES = (
        (1, "Intelektual"),
        (2, "Maxsus tayyorgarlik"),
        (3, "Shaxsiy (ruhiy, psixologik)"),
        (4, "Jismoniy"),
    )

    status = models.IntegerField(choices=STATUS_CHOICES)
    image = models.ImageField(upload_to="imsj_images/")
    text = models.TextField()

    def __str__(self):
        return f"IMSJ {self.get_status_display()} - {self.text}"


class Intelekt(models.Model):
    savol_matni = models.TextField()

    def __str__(self):
        return self.savol_matni[:50]


class IntelektVariant(models.Model):
    savol = models.ForeignKey(Intelekt, related_name="variantlar", on_delete=models.CASCADE)
    matn = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.savol.savol_matni} - {self.matn}"


class Maxsus(models.Model):
    savol_matni = models.CharField(max_length=255)

    def __str__(self):
        return self.savol_matni


class MaxsusVariant(models.Model):
    savol = models.ForeignKey(Maxsus, related_name="variantlar", on_delete=models.CASCADE)
    matn = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.savol.savol_matni} - {self.matn}"
