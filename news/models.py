from django.db import models

from news.managers import ArticleManager
# Create your models here.


class Article(models.Model):
    """
    A news Article!
    """

    objects = ArticleManager()

    title = models.CharField(blank=True, null=True, max_length=1000)
    author = models.CharField(blank=True, null=True, max_length=1000)
    description = models.CharField(blank=True, null=True, max_length=1000)
    url = models.CharField(blank=True, null=True, max_length=1000)
    content = models.CharField(max_length=2000, blank=True, null=True)
