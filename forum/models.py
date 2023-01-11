from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):  # Definiujemy funkcje, która zwraca tytuł wpisu
        return self.title


class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "answers"
