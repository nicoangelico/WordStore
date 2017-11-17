from django.conf.urls import url
from . import views

app_name = 'wordstore'
urlpatterns = [
    # ex: /wordstore/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<word_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^login$', views.login, name='login'),
]