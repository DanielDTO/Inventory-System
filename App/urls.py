from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', index, name='index'), #connect index page to our function

    url(r'^get_desktops$', get_desktops, name = 'get_desktops'),
    url(r'^get_laptops$', get_laptops, name= 'get_laptops'),
    url(r'^get_mobiles$', get_mobiles, name = 'get_mobiles'),
    url(r'^get_stationary$', get_stationary, name = 'get_stationary'),

    url(r'^add_desktop$', add_desktop, name = 'add_desktop'),
    url(r'^add_laptop$', add_laptop, name = 'add_laptop'),
    url(r'^add_mobile$', add_mobile, name = 'add_mobile'),
    url(r'^add_stationary$', add_stationary, name = 'add_stationary'),

    url(r'^edit_desktop/(?P<pk>\d+)$', edit_desktop, name = 'edit_desktop'),
    url(r'^edit_laptop/(?P<pk>\d+)$', edit_laptop,  name = 'edit_laptop'),
    url(r'^edit_mobile/(?P<pk>\d+)$', edit_mobile, name = 'edit_mobile'),
    url(r'^edit_stationary/(?P<pk>\d+)$', edit_stationary, name = 'edit_stationary'),

    url(r'^del_desktop/(?P<pk>\d+)$', del_desktop, name = 'del_desktop'),
    url(r'^del_laptop/(?P<pk>\d+)$', del_laptop, name = 'del_laptop'),
    url(r'^del_mobile/(?P<pk>\d+)$', del_mobile, name = 'del_mobile'),
    url(r'^del_stationary/(?P<pk>\d+)$', del_stationary, name = 'del_stationary'),

    url(r'^get_all$', get_all, name = 'get_all')





]