from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^relationships/', include('relationships.urls')),
)
