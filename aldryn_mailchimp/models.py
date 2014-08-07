# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class SubscriptionPlugin(CMSPlugin):

    list_id = models.CharField(_('List ID'), max_length=20)
    assign_language = models.BooleanField(
        _('Save user\'s language'), default=True, help_text=_('Save the user\'s language based on the page language'))

    def __unicode__(self):
        return str(self.list_id)


class CampaignManager(models.Manager):
    def published(self):
        return self.filter(send_time__isnull=False, hidden=False)


class Campaign(models.Model):
    cid = models.CharField(_('campaign id'), max_length=255, editable=False)
    mc_title = models.CharField(_('campaign title'), max_length=255, editable=False)
    subject = models.CharField(_('subject'), max_length=255, editable=False)
    send_time = models.DateTimeField(_('time sent'), blank=True, null=True, editable=False)
    content_text = models.TextField(_('content text'), blank=True, null=True, editable=False)
    content_html = models.TextField(_('content HTML'), blank=True, null=True, editable=False)
    slug = models.SlugField(_('slug (generated)'), editable=False)
    hidden = models.BooleanField(_('hidden'), default=False)

    objects = CampaignManager()

    class Meta:
        ordering = ['-send_time']

    def __str__(self):
        return '%s (%s)' % (self.mc_title, self.subject)

    def get_absolute_url(self):
        return reverse('mailchimp_campaign_detail', kwargs={'pk': self.pk, 'slug': self.slug})


class CampaignArchivePlugin(CMSPlugin):
    count = models.PositiveSmallIntegerField(
        _('count'), null=True, blank=True, help_text=_('Leave blank to display all')
    )


class SelectedCampaignsPlugin(CMSPlugin):
    campaigns = models.ManyToManyField(Campaign)

    def copy_relations(self, old_instance):
        self.campaigns = old_instance.campaigns.all()
