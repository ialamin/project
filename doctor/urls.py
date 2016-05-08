from django.conf.urls import url
from django.contrib import admin
from . import views





urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^hello/$', views.index, name='hello'), no more "hello function"
    url(r'^(?P<doctor_id>[0-9]+)/$', views.doctor, name='doctor')
]
