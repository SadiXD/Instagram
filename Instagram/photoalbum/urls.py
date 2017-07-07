from django.conf.urls import url
from .views import PhotoDetail


app_name = 'comment'

urlpatterns = [
    url(r'^$', PhotoDetail.as_view(), name='photo_detail'),
]
