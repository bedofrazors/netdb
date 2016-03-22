from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/(?P<id>[0-9]+)$', views.create, name='create'),
    url(r'^read/(?P<id>[0-9]+)$', views.read, name='read'),
    url(r'^update/(?P<id>[0-9]+)$', views.update, name='update'),
    url(r'^delete/(?P<id>[0-9]+)$', views.delete, name='delete'),
]
