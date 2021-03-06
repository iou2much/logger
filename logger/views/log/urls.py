from django.conf.urls import patterns, include, url
#from logger.views import list_sys
from logger.views.log.log import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'logger.views.home', name='home'),
    # url(r'^logger/', include('logger.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

     url(r'list/$', ls_log),
     url(r'remove/$', rm_log),
     url(r'add/$', add_log),
     url(r'map/$', map_key_name),
)
