from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'data.views.home', None, name='home'),
    url(r'source/$', 'data.views.source', None, name='source'),
    url(r'mapping/$', 'data.views.mapping', None, name='mapping'),    
    url(r'target/$', 'data.views.target', None, name='target'),
    url(r'database/$', 'data.views.database', None, name='database'),
    url(r'populate_source/$', 'data.views.populate_source', None, name='populate_source'),
)