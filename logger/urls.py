from django.conf.urls import patterns, include, url
import logger.views.system.urls as sys_url
import logger.views.module.urls as mod_url
import logger.views.log.urls as log_url
import logger.views.common.urls as common_url
import logger.views.common.common as common

from django.conf.urls.static import static 
 
urlpatterns = patterns('',
    url(r'^sys/', include(sys_url)),
    url(r'^module/', include(mod_url)),
    url(r'^log/', include(log_url)),
    url(r'^index/', include(common_url)),
    url(r'', common.index),
)
