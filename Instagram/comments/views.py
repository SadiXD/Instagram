from django.shortcuts import redirect, render
from django.views import View
from .forms import CommentForm
from photoalbum.models import Photo


class CommentValidation(View):
    def post(self, request, id):
        form = CommentForm(request.POST)
        photo = Photo.objects.get(id=id)
        if form.is_valid():
            form.save(request)
            form = CommentForm()
            return redirect('/photo/{}'.format(photo.id))
        else:
            photo = Photo.objects.get(id=request.POST['photo'])
            return render(request, 'photoalbum/photo.html', {'photo': photo, 'form': form})
