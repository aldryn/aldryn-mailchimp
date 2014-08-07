# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .views import SubscriptionView
from .models import Campaign, SubscriptionPlugin, CampaignArchivePlugin, SelectedCampaignsPlugin
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


class CampaignArchive(CMSPluginBase):
    render_template = 'aldryn_mailchimp/plugins/campaign_archive.html'
    name = _('Campaign Archive')
    module = _('MailChimp')
    model = CampaignArchivePlugin

    def render(self, context, instance, placeholder):
        objects = Campaign.objects.published()
        if instance.count:
            objects = objects[:instance.count]
        context['object_list'] = objects
        return context

plugin_pool.register_plugin(CampaignArchive)


class SelectedCampaigns(CMSPluginBase):
    render_template = 'aldryn_mailchimp/plugins/selected_campaigns.html'
    name = _('Selected Campaigns')
    module = _('MailChimp')
    model = SelectedCampaignsPlugin

    def render(self, context, instance, placeholder):
        context['object_list'] = instance.campaigns.objects.all()
        return context

plugin_pool.register_plugin(SelectedCampaigns)
