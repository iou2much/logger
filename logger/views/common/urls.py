from django.conf.urls import patterns, include, url
from logger.views.common.common import *

urlpatterns = patterns('',
     url(r'index/$', index),
     #url(r'remove/$', rm_log),
     #url(r'add/$', add_log),
)
