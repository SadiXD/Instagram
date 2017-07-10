from django.conf.urls import url

from .views import UserLoginView, UserLogoutView, UserCreateView, InstagramView

urlpatterns = [
    url(r"^login/", UserLoginView.as_view(), name="login-user"),
    url(r'^logout/', UserLogoutView.as_view(), name="logout_view"),
    url(r'^add_user/', UserCreateView.as_view(), name="add-user"),
    url(r'^instagram/', InstagramView.as_view(), name="instagram"),
]