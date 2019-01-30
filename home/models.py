from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    posted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post_desc = models.CharField(
        verbose_name='Description', max_length=100, blank=True)
    post_body = models.CharField(
        verbose_name='Body', max_length=1000, blank=True)
    posted_on = models.DateTimeField(
        verbose_name='Posted on', auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
