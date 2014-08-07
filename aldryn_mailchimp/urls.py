# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('aldryn_mailchimp.views',
    url(r'^(?P<pk>[0-9]+)/(?P<slug>[\w.@+-]+)/$', 'campaign_detail', name='mailchimp_campaign_detail'),
)
