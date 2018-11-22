from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListaMenus, name ='ListaMenus'),
    url(r'^ventas/nueva/$', views.menu_nuevo, name='menu_nuevo'),
    ]
