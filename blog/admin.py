from django.contrib import admin
from .models import Categorie, Article, Commentaire


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nomCategorie', 'description', 'dateCreation')
    search_fields = ('nomCategorie', 'description')
    list_filter = ('dateCreation',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication', 'publier', 'categorie', 'auteur')
    search_fields = ('titre', 'contenu')
    list_filter = ('date_publication', 'publier', 'categorie')

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('message', 'dateCommentaire', 'article', 'username')
    search_fields = ('message',)
    list_filter = ('dateCommentaire',)

