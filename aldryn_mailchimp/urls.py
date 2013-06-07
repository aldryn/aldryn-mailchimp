# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from aldryn_mailchimp.views import SubscriptionView

urlpatterns = patterns(
    '',
    url(r'^subscribe/$', SubscriptionView.as_view(), name='subscription'),
)
