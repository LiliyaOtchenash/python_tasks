from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<tab_num>[0-9]+)/$', views.det, name='det'),
    url(r'^(?P<tab_num>[0-9]+)/res/$', views.res, name='res'),
    url(r'^(?P<tab_num>[0-9]+)/vot/$', views.vot, name='vot')
    
]
