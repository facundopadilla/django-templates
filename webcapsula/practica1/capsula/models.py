from django.db import models

# Create your models here.

class Service(models.Model):
    icon = models.CharField(max_length=100, verbose_name="Icono")
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return self.title

class About(models.Model):
    image = models.ImageField(verbose_name="Imagen", upload_to="about")
    title = models.CharField(max_length=100, verbose_name="Título")
    subtitle = models.CharField(max_length=100, verbose_name="Subtítulo")
    description = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return self.title

class Team(models.Model):
    image = models.ImageField(verbose_name="Foto", upload_to="team")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=200, verbose_name="Descripción")
    linkedin = models.TextField(verbose_name="LinkedIn")
    github = models.TextField(verbose_name="GitHub")
    facebook = models.TextField(verbose_name="Facebook")

    def __str__(self):
        return self.name

class Client(models.Model):
    image = models.ImageField(verbose_name="Foto", upload_to="client")

class Portfolio(models.Model):
    image = models.ImageField(verbose_name="Foto del proyecto", upload_to="portfolio")
    title = models.CharField(max_length=100, verbose_name="Título")
    subtitle = models.CharField(max_length=100, verbose_name="Subtítulo")
    project_name = models.CharField(max_length=200, verbose_name="Nombre del proyecto")
    project_data = models.CharField(max_length=300, verbose_name="Datos específicos del proyecto")
    project_image = models.ImageField(verbose_name="Foto del proyecto")
    project_description = models.TextField(verbose_name="Descripción del proyecto")
    project_date = models.DateField(verbose_name="Fecha de inicio")
    project_client = models.CharField(max_length=100)
    project_category = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name

