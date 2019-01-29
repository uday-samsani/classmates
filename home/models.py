from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import Account
#Account = get_user_model()


class Post(models.Model):
    user = models.ManyToManyField(Account)
    title = models.CharField(max_length=40, blank=True)
    description = models.CharField(max_length=40, blank=True)
    body = models.CharField(max_length=500, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
