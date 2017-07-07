from django.conf.urls import url
from .views import PhotoDetail, PhotoAddView


app_name = 'comment'

urlpatterns = [
    url(r'^$', PhotoDetail.as_view(), name='photo_detail'),
    url(r'^add_photo/', PhotoAddView.as_view(), name='photo_add'),
]
