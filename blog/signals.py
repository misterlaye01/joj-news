from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Commentaire


@receiver(post_save, sender=Commentaire)
def notifier_nouveau_commentaire(sender, instance, created, **kwargs):
    if not created:
        return

    article = instance.article
    titre = article.titre

    subject = f"Nouveau commentaire sur : {titre}"
    message = (
        f"Un nouveau commentaire a ete publie sur l'article '{titre}'.\n\n"
        f"Auteur : {instance.username}\n"
        f"Message : {instance.message}\n"
        f"Date : {instance.dateCommentaire}"
    )

    admin_emails = [email for _, email in getattr(settings, "ADMINS", [])]
    if not admin_emails:
        return

    from_email = getattr(settings, "DEFAULT_FROM_EMAIL", "webmaster@localhost")
    send_mail(subject, message, from_email, admin_emails)
