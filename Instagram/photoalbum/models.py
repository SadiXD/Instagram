from django.db import models
from datetime import datetime
from Instagram.Instagram.settings import AUTH_USER


class Photo(models.Model):
    image = models.ImageField(upload_to='photos', verbose_name='Photo')
    user = models.ForeignKey(AUTH_USER, related_name='photos')
    description = models.CharField(max_length=243, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-added']


    @property
    def time_since_add(self):
        delta_time = (datetime.now() - self.added)
        return delta_time.days or delta_time.hour or delta_time.minute or 'Now'

    @property
    def comment_count(self):
        return len(self.objects.comments.all())
