from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from photoalbum.models import Photo
from user.models import InstagramUser
from .forms import UserLoginForm, UserCreateForm


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm
        ctx = {
            "form": form
        }
        return render(request, "user/login_user.html", ctx)

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('/instagram/')
        else:
            return render(request, "user/login_user.html", {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = "user/user_form.html"
    success_url = reverse_lazy("login-user")


class InstagramView(View):
    def get(self, request):
        photo_list = Photo.objects.all()
        ctx = {
            'photo_list': photo_list
        }
        return render(request, 'user/instagram.html', ctx)


class UserView(View):
    def get(self, request, id):
        user = InstagramUser.objects.get(id=id)
        photo_list = Photo.objects.filter(user=user)
        return render(request, 'user/user_detail.html', {'user': user, 'photo_list': photo_list})
