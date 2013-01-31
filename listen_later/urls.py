from django.conf.urls import patterns, include, url
from django.contrib import admin
from audio.models import Audio

admin.autodiscover()
admin.site.register(Audio)

urlpatterns = patterns('',
    url(r'^', include('audio.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
