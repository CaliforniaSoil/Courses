from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^(?P<course_id>\d+)/remove$', views.remove),
    url(r'^(?P<course_id>\d+)/destroy$', views.destroy),
]