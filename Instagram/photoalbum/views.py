from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from .models import Photo
from comments.forms import CommentForm
from photoalbum.forms import PhotoAddForm
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


class PhotoDetail(View):
    def get(self, request, id):
        photo = Photo.objects.get(id=id)
        form = CommentForm(initial={'photo': id})
        return render(request, 'photoalbum/photo.html', {'photo': photo, 'form': form})


class PhotoAddView(View):
    def get(self, request):
        form = PhotoAddForm()
        return render(request, 'photoalbum/photo_form.html', {'form': form})

    def post(self, request):
        form = PhotoAddForm(request.POST, request.FILES)
        if form.is_valid():
            # instance = Photo(image=request.FILES['image'])
            # instance.save()
            form.save(request)
            return HttpResponseRedirect('/instagram/')
        else:
            form = PhotoAddForm()
        return render(request, 'photoalbum/photo_form.html', {'form': form})

