from django.shortcuts import render
from .models import Article
# Create your views here.
  
def liste_article(request):
    articles = Article.objects.all()

    context = {
        'articles' : articles
    }

    return render(request, 'liste_article.html',context)