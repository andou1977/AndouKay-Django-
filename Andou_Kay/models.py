from django.db import models


# Create your models here.
class Utilisateur(models.Model):
    Nom = models.CharField(max_length=35)
    Prenom = models.CharField(max_length=35)
    Sexe = models.CharField(max_length=35)
    Pseudo = models.CharField(max_length=35)
    Password = models.CharField(max_length=35)
    Droit = models.CharField(max_length=35)
    Date = models.DateField()

    class Meta:
        ordering = ('Nom',)

    def __str__(self):
        return self.Nom


class Proprietaire(models.Model):
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)
    Telephone = models.CharField(max_length=35)
    # valeur nombre de piece padwe superieur a 2 chiffres
    Nombre_De_Piece = models.IntegerField()
    Adresse = models.CharField(max_length=50)
    Cout = models.CharField(max_length=50)
    Image = models.ImageField(blank=True, null=True)
    Description = models.TextField(max_length=900)
    Duree = models.CharField(max_length=40)
    Monnaie = models.CharField(max_length=30,default='Monnaie value')
    Departement = models.CharField(max_length=35)
    Date_du_jour = models.DateField()
    Sexe = models.CharField(max_length=20)
    type = models.CharField(max_length=30,default='DEFAULT VALUE2')
    Nif = models.CharField(max_length=30, default='DEFAULT Nif')
    # Longitude = models.DecimalField(decimal_places=30, max_digits=30)
    # Latitude = models.DecimalField(decimal_places=30, max_digits=30)

    class Meta:
        ordering = ('Nom',)

    def __str__(self):
        return self.Nom
