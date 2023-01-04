from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, default='', blank=True)
    bio = models.TextField(default='', blank=True)

    def create_profile(sender, **kwargs):  # Funckja, ktora tworzy profile użytkownika
        user = kwargs["instance"]
        if kwargs["created"]:
            user_profile = UserProfile(user=user)
            user_profile.save()

    post_save.connect(create_profile, sender=User)

    def __str__(self):  # Definiujemy funkcje, która zwraca tytuł wpisu
        return self.user.username
