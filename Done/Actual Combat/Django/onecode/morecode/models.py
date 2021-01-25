from django.db import models


# Create your models here.


class Articles(models.Model):
    article_title = models.CharField(max_length=64)
    article_detail = models.CharField(max_length=1000)
    article_details = models.TextField(blank=True, null=True)
