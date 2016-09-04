from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.create),
    url(r'^destroy/(?P<id>\d+)$', views.delete),
    url(r'^delete/(?P<id>\d+)$', views.deleting),
    
]

