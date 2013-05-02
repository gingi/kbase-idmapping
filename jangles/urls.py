from django.conf.urls import patterns, include, url

# from tastypie docs
from django.conf.urls.defaults import *
from tastypie.api import Api
from idmapping.api import PollResource,ChoiceResource
v1_api = Api(api_name='v1')
v1_api.register(PollResource())
v1_api.register(ChoiceResource())


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jangles.views.home', name='home'),
    # url(r'^jangles/', include('jangles.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # from tastypie docs
    (r'^api/', include(v1_api.urls)),
)
