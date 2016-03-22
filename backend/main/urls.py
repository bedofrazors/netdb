from django.conf.urls import url, include

from . import views
from organisation import views as organisation

urlpatterns = [
    url(r'^$', views.index, name='index'),
]