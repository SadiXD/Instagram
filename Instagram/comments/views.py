from django.shortcuts import redirect
from django.views import View
from .forms import CommentForm
from ..photoalbum.forms import Photo


class CommentValidation(View):
    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('photo_detail')
        else:
            photo = Photo.objects.get(id=request.POST['photo'])
            return render(request, 'photoalbum/photo.html', {'photo': photo, 'form': form})
