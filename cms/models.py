# cms/models.py
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    content = models.TextField(verbose_name="Treść")
    date = models.DateField(auto_now_add=True, verbose_name="Data")

    class Meta:
        verbose_name = "Aktualność"
        verbose_name_plural = "Aktualności"

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    content = models.TextField(verbose_name="Treść")
    date = models.DateField(auto_now_add=True, verbose_name="Data")

    class Meta:
        verbose_name = "Ogłoszenie"
        verbose_name_plural = "Ogłoszenia"

    def __str__(self):
        return self.title


class Intention(models.Model):
    name = models.CharField(max_length=200, verbose_name="Imię / Nazwa")
    prayer = models.TextField(verbose_name="Treść intencji")
    date = models.DateField(auto_now_add=True, verbose_name="Data")

    class Meta:
        verbose_name = "Intencja"
        verbose_name_plural = "Intencje"

    def __str__(self):
        return self.name
