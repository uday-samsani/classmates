from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    posted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    liked_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post_desc = models.CharField(max_length=40, blank=True)
    post_body = models.CharField(max_length=500, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
