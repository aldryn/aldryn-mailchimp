# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .views import SubscriptionView
from .models import SubscriptionPlugin
from .forms import SubscriptionPluginForm


class SubscriptionCMSPlugin(CMSPluginBase):

    render_template = 'aldryn_mailchimp/snippets/_subscription.html'
    name = _('Subscription')
    model = SubscriptionPlugin
    module = _('MailChimp')

    def render(self, context, instance, placeholder):
        request = context['request']
        context['form'] = SubscriptionPluginForm(initial={'plugin_id': instance.pk,
                                                          'redirect_url': request.get_full_path()})
        return context

    def get_plugin_urls(self):
        return patterns('',
            url(r'^subscribe/$', SubscriptionView.as_view(), name='aldryn-mailchimp-subscribe'),
        )

plugin_pool.register_plugin(SubscriptionCMSPlugin)
