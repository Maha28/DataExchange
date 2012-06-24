from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #Common
    url(r'^$', 'data.views.home', name='home'),                   
                       
    #Database
    url(r'^database/$', 'data.views.database', name='database'),
    url(r'^database/clear_all/$', 'data.views.clear_all', name='clear_all'),                     
    
    #Source                   
    url(r'^source/$', 'data.views.source', name='source'),
    url(r'^database/create_new_source/(?P<view_name>\w+)/$', 'data.views.create_new_source', name='create_new_source'),
    url(r'^database/delete_source/(?P<view_name>\w+)/(?P<source_id>\w+)/$', 'data.views.delete_source', name='delete_source'),
    url(r'^database/populate_source/(?P<view_name>\w+)/(?P<source_id>\w+)/$', 'data.views.populate_source', name='populate_source'),
    url(r'^database/clear_source/(?P<view_name>\w+)/(?P<source_id>\w+)/$', 'data.views.clear_source', name='clear_source'),    
    
    #Mapping
    url(r'^mapping/$', 'data.views.mapping', name='mapping'),
    url(r'^database/populate_mapping/(?P<view_name>\w+)/$', 'data.views.populate_mapping', name='populate_mapping'),
    url(r'^database/clear_mapping/(?P<view_name>\w+)/$', 'data.views.clear_mapping', name='clear_mapping'),    
   
    #Equal    
    url(r'^equal/$', 'data.views.equal', name='equal'),   
    url(r'^database/generate_equal/(?P<view_name>\w+)/$', 'data.views.generate_equal', name='generate_equal'),
    url(r'^database/clear_equal/(?P<view_name>\w+)/$', 'data.views.clear_equal', name='clear_equal'),      
    url(r'^database/update_mapping_from_equal/(?P<view_name>\w+)/$', 'data.views.update_mapping_from_equal', name='update_mapping_from_equal'),  
    url(r'^database/update_source_from_equal/(?P<view_name>\w+)/$', 'data.views.update_source_from_equal', name='update_source_from_equal'),        
   
    #Queries   
    url(r'^queries/$', 'data.views.queries', name='queries'),
    url(r'^queries/(?P<source_id>\w+)/$', 'data.views.queries', name='queries'),
   
    #Target   
    url(r'^target/$', 'data.views.target', name='target'),   
)