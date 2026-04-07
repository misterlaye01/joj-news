from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.ConnexionLoginView.as_view(), name='login'),
    path('logout/', views.DeconnexionLogoutView.as_view(), name='logout'),

    path('', views.ArticleListView.as_view(), name = 'liste_article'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='detail_article'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='update_comment'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
]
