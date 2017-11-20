from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'wordstore'

urlpatterns = [
    # ex: /wordstore/
    url(r'^$', views.index, name='index'),
    url(r'^worduser$', views.userWord, name='userword'),
    url(r'^detail/(?P<word_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^login$', login, {'template_name':'wordstore/login.html'}, name='login'),
    url(r'^newuser$', views.newUser, name='newuser'),
]