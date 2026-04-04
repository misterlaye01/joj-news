from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categorie(models.Model):
    nomCategorie = models.CharField(max_length=255)
    description = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomCategorie
 


class Article(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='imageArticle/', null=True, blank=True)
    publier = models.BooleanField(default=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    dateCommentaire = models.DateTimeField(auto_now_add=True)
    message = models.TextField()    
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"Commentaire sur {self.username} à {self.dateCommentaire}"
    
