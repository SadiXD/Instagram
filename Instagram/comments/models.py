from django.db import models
from Instagram.Instagram.settings import AUTH_USER
from ..photoalbum.models import Photo


class Comment(models.Model):
    user = models.ForeignKey(AUTH_USER)
    photo = models.ForeignKey(Photo, related_name='comments')
    content = models.TextField(verbose_name='Comment')
    added = models.DateTimeField(auto_now_add=True)
