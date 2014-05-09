from django.conf.urls import patterns, include, url
from django.contrib import admin
from Gestor.views import ingresar, home, proyecto1, proyectos
admin.autodiscover()
urlpatterns = patterns('',	
     url(r'^ingresar/', ingresar),
     url(r'^home/', home),
     url(r'^proyecto1/', proyecto1),
     url(r'^proyectos/', proyectos),
)




