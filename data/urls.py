from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'data.views.home', name='home'),
    url(r'source/$', 'data.views.source', name='source'),
)