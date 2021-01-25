from django.conf.urls import url
from django.urls import path

from . import mydjangoDemo01

urlpatterns = [
    url('hello/', mydjangoDemo01.hello),
    path('runoob/',mydjangoDemo01.runoob),
    path('run',mydjangoDemo01.run)
]