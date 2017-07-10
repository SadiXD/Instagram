from .models import Photo
from comments.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from photoalbum.forms import PhotoAddForm
from photoalbum.models import Photo


class PhotoDetail(LoginRequiredMixin, View):
    def get(self, request, id):
        photo = Photo.objects.get(id=id)
        form = CommentForm(initial={'photo': id})
        return render(request, 'photoalbum/photo.html', {'photo': photo, 'form': form})


class PhotoAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = PhotoAddForm()
        return render(request, 'photoalbum/photo_form.html', {'form': form})

    def post(self, request):
        form = PhotoAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return redirect('/instagram/')
        else:
            form = PhotoAddForm()
        return render(request, 'photoalbym/photo_form.html', {'form': form})