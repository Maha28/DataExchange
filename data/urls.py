from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'data.views.home', name='home'),
    url(r'source/$', 'data.views.source', name='source'),
    url(r'mapping/$', 'data.views.mapping', name='mapping'),    
    url(r'target/$', 'data.views.target', name='target'),
    url(r'database/$', 'data.views.database', name='database'),
    url(r'database/populate_source$', 'data.views.populate_source', name='populate_source'),
    url(r'database/clear_source$', 'data.views.clear_source', name='clear_source'),
)