from django.conf.urls.defaults import *

urlpatterns = patterns('todo.views',
    url(r'^$', 'index', name='index'),
    url(r'^ver_articulo/(?P<id>\d+)/$', 'ver_detalle', name='ver'),

)