from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #Common
    url(r'^$', 'data.views.home', name='home'),                   
                       
    #Database
    url(r'^database/$', 'data.views.database', name='database'),
    url(r'^database/populate_source/$', 'data.views.populate_source', name='populate_source'),
    url(r'^database/clear_source/$', 'data.views.clear_source', name='clear_source'),
    url(r'^database/populate_mapping/$', 'data.views.populate_mapping', name='populate_mapping'),
    url(r'^database/clear_mapping/$', 'data.views.clear_mapping', name='clear_mapping'),    
    url(r'^database/generate_equal/$', 'data.views.generate_equal', name='generate_equal'),
    url(r'^database/clear_equal/$', 'data.views.clear_equal', name='clear_equal'), 
    url(r'^database/clear_all/$', 'data.views.clear_all', name='clear_all'),                     
    
    #Source                   
    url(r'^source/$', 'data.views.source', name='source'),
    url(r'^source/populate_source/$', 'data.views.populate_source_from_source', name='populate_source_from_source'),
    url(r'^source/clear_source/$', 'data.views.clear_source_from_source', name='clear_source_from_source'),
    
    #Mapping
    url(r'^mapping/$', 'data.views.mapping', name='mapping'),
    url(r'^mapping/populate_mapping/$', 'data.views.populate_mapping_from_mapping', name='populate_mapping_from_mapping'),
    url(r'^mapping/clear_mapping/$', 'data.views.clear_mapping_from_mapping', name='clear_mapping_from_mapping'),  
    
    #Equal    
    url(r'^equal/$', 'data.views.equal', name='equal'),    
    url(r'^equal/generate_equal/$', 'data.views.generate_equal_from_equal', name='generate_equal_from_equal'),
    url(r'^equal/clear_equal/$', 'data.views.clear_equal_from_equal', name='clear_equal_from_equal'),     
    #Target   
    url(r'^target/$', 'data.views.target', name='target'),
       
)