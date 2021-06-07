from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(default="default.jpg",blank=True)
    def __str__(self):
        return self.title
    def slep(self):
    	return self.body[:10]
        
class Formule(models.Model):
	name=models.CharField(max_length=200)
	CNE=models.CharField(max_length=10)
	CNI=models.CharField(max_length=10)
	telephone=models.IntegerField()
	email=models.EmailField(max_length=254)
	demande=models.TextField()

class Formule1(models.Model):
    choix_liste=(
        ("1","pavion1"),
        ("2","pavion2"),
        ("3","pavion3")
        )
    nom=models.CharField(max_length=50)
    chambre=models.IntegerField()
    demande=models.TextField()
    pavion=models.CharField( max_length=7,choices=choix_liste)

class Formule2(models.Model):
    email=models.EmailField(max_length=254)








 



