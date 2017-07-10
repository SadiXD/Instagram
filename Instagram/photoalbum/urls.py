from django.conf.urls import url
from .views import PhotoAddView, PhotoDetail


app_name = 'comment'

urlpatterns = [
    url(r'^add_photo', PhotoAddView.as_view(), name="photo_add"),
    url(r'^photo/(?P<id>(\d)+)/$', PhotoDetail.as_view(), name='photo_detail'),
]
