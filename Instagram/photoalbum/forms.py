from django.forms import ModelForm
from .models import Photo


class PhotoAddForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description']

    def save(self, request, *args, **kwargs):
        self.instance.user = request.user
        return super(PhotoAddForm, self).save(*args, **kwargs)

