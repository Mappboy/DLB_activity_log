#! /usr/bin/env python2.7
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.views import serve
from django.contrib import admin
from django.contrib.auth import views as auth_views
from DLB_activity_log.home.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),

    # static
    url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), serve,
        {'show_indexes': True, 'insecure': False}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^create_dataset/', CreateDataset.as_view(), name='create_dataset'),
    url(r'^datasets/',DatasetList.as_view()),
    url(r'^edit_dataset/(?P<dataset>.*)', UpdateDataset.as_view(), name='edit_dataset'),
    url(r'^del_dataset/(?P<dataset>.*)', DelDataset.as_view(), name='del_dataset'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )