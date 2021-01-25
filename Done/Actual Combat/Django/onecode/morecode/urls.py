from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path('^<int:article_id>/', article_detail),
    # re_path('1/', article_detail),
    # re_path('insert/', articleinsert, name='article_insert'),
    re_path('^$', article_list, name='article_list'),
]
