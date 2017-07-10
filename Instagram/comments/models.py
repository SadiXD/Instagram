from django.db import models
from django.conf import settings
from photoalbum.models import Photo


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ForeignKey(Photo, related_name='comments')
    content = models.TextField(verbose_name='Comment')
    added = models.DateTimeField(auto_now_add=True)
