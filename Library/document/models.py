from django.db import models

# Create your models here.
class Domaine(models.Model):
    name = models.CharField('Domaines', max_length=50)
    slug = models.SlugField(max_length = 50)
    def __str__(self):
        return self.name

class Ouvrage(models.Model):
    titre = models.CharField(max_length = 100)
    slug = models.SlugField(max_length=100)
    image_cover = models.ImageField(upload_to = 'img', blank = True, null = True)
    auteur = models.CharField(max_length=50)
    langue = models.CharField(max_length=50)
    domaine = models.ManyToManyField(Domaine, related_name='ouvrages')
    nombre_pages = models.CharField(max_length=50)
    editeur = models.CharField(max_length=100)
    description = models.TextField()
    pdf = models.FileField(upload_to='pdf')
    livre = models.BooleanField(default=False)
    memoire = models.BooleanField(default=False)
    magazine_et_revue = models.BooleanField(default=False)

    def __str__(self):
        return self.titre


# class RechercheOuvrage(models.Model):
#     nom_ouvrage = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name_ouvrage