from django.conf.urls import url
from . import views

app_name = 'wordstore'

urlpatterns = [
    # ex: /wordstore/
    url(r'^', views.index, name='index'),
    url(r'^(?P<username>\w+)', views.userWord, name='userword'),
    url(r'^(?P<word_id>[0-9]+)', views.detail, name='detail'),
    url(r'^login', views.login, name='login'),
    url(r'^newuser', views.newUser, name='newuser'),
]