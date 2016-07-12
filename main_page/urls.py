from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'contact_to', views.post_contact, name='contact_to'),
    url(r'certs', views.certs, name='certifucates'),
    url(r'costservice', views.cost_service, name='cost_service'),
]