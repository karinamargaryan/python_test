from django.conf.urls import url
from main.views import insert,update,delete,index


urlpatterns = [
    url(r'^$', index ,name="index"),
    url(r'^insert/$', insert ,name="insert"),
    url(r'^update/$', update ,name="update"),
    url(r'^delete/(?P<pk>\d+)/$', delete ,name="delete"),
]