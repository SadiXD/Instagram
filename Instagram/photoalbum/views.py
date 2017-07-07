from django.shortcuts import render
from django.views import View
from .models import Photo
from ..comments.forms import CommentForm


class PhotoDetail(View):
    def get(self, request, id):
        photo = Photo.objects.get(id=id)
        form = CommentForm(initial={'photo': id})
        return render(request, 'photoalbum/photo.html', {'photo': photo, 'form': form})
