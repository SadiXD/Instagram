from django.conf.urls import url
from .views import CommentValidation


app_name = 'comment'

urlpatterns = [
    url(r'^$', CommentValidation.as_view(), name='comment_valid'),
]
