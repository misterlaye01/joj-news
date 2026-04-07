from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Article, Commentaire
from .forms import SignUpForm, LoginForm, CommentForm


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('liste_article')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('liste_article')
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})

class ConnexionLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = LoginForm


class DeconnexionLogoutView(LogoutView):
    next_page = 'login'


class ArticleListView(ListView):
    model = Article
    template_name = 'liste_article.html'
    paginate_by = 10
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(publier=True).order_by('-date_publication')


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'detail_article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Commentaire.objects.filter(article=self.object).order_by('dateCommentaire')
        context['form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.article = self.object
            commentaire.username = request.user
            commentaire.save()
            return redirect("detail_article", pk=self.object.pk)

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Commentaire
    form_class = CommentForm
    template_name = 'update_comment.html'
    
    def get_success_url(self):
        return reverse('detail_article', kwargs={'pk': self.object.article.pk}) #type: ignore


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Commentaire
    template_name = 'delete_comment.html'

    def get_success_url(self):
        return reverse('detail_article', kwargs={'pk': self.object.article.pk}) #type: ignore
