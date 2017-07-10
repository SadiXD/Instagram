from django.conf.urls import url
from .views import CommentValidation


app_name = 'comment'

urlpatterns = [
    url(r'^photo/(?P<id>(\d)+)/comment_valid$', CommentValidation.as_view(), name='comment_valid'),
]
