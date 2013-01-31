from django.conf.urls import patterns, include, url
from django.contrib import admin
from audio.models import Audio

admin.autodiscover()
admin.site.register(Audio)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'listen_later.views.home', name='home'),
    # url(r'^listen_later/', include('listen_later.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
