# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from aldryn_mailchimp import models
from aldryn_mailchimp import forms


class SubscriptionPlugin(CMSPluginBase):

    render_template = 'aldryn_mailchimp/subscription.html'
    name = _('Subscription')
    model = models.SubscriptionPlugin
    module = _('MailChimp')

    def render(self, context, instance, placeholder):
        request = context['request']
        context['form'] = forms.SubscriptionForm(initial={'list_id': instance.list_id,
                                                          'redirect_url': request.get_full_path()})
        return context

plugin_pool.register_plugin(SubscriptionPlugin)
