from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'photo']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['photo'].widet.attrs['hidden'] = True

    def save(self, request, commit=True, *args, **kwargs,):
        self.instance.user = request.user
        super(CommentForm, self).save(*args, **kwargs)

