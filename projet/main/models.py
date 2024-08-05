from django.db import models


class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Ouvrage(models.Model):
    titre = models.CharField(max_length=200)
    date_publication = models.DateField()
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
