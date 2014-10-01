# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey


class SubscriptionPlugin(CMSPlugin):

    list_id = models.CharField(_('List ID'), max_length=20)
    assign_language = models.BooleanField(
        _('Save user\'s language'), default=True, help_text=_('Save the user\'s language based on the page language'))

    def __unicode__(self):
        return unicode(self.list_id)


class CampaignManager(models.Manager):
    def published(self):
        return self.filter(send_time__isnull=False, hidden=False)


class Category(Sortable):
    name = models.CharField(_('name'), max_length=255)
    smart_match = models.BooleanField(
        _('Matching'), default=True, help_text=_('Match incoming campaigns to categories based on keywords')
    )

    class Meta(Sortable.Meta):
        ordering = ('order', 'name')
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __unicode__(self):
        return unicode(self.name)


class Keyword(Sortable):
    value = models.CharField(_('value'), max_length=255, unique=True)
    category = SortableForeignKey(Category, verbose_name=_('category'))
    scope_name = models.BooleanField(_('search in campaign name'), default=True)
    scope_subject = models.BooleanField(_('search in campaign subject'), default=False)
    scope_content = models.BooleanField(_('search in campaign content'), default=False)

    class Meta(Sortable.Meta):
        ordering = ('order', 'value')
        verbose_name = _('Keyword')
        verbose_name_plural = _('Keywords')

    def __unicode__(self):
        return u'%s (%s)' % (self.value, self.category.name)


class Campaign(models.Model):
    cid = models.CharField(_('campaign id'), max_length=255, editable=False)
    mc_title = models.CharField(_('campaign title'), max_length=255, editable=False)
    subject = models.CharField(_('subject'), max_length=255, blank=True, null=True, editable=False)
    display_name = models.CharField(_('display name'), max_length=255, blank=True, null=True)
    send_time = models.DateTimeField(_('time sent'), blank=True, null=True, editable=False)
    content_text = models.TextField(_('content text'), blank=True, null=True, editable=False)
    content_html = models.TextField(_('content HTML'), blank=True, null=True, editable=False)
    slug = models.SlugField(_('slug (generated)'), editable=False)
    hidden = models.BooleanField(_('hidden'), default=False)
    category = models.ForeignKey(Category, blank=True, null=True, help_text=_('leave empty to auto-match on import'))

    objects = CampaignManager()

    class Meta:
        ordering = ['-send_time']
        verbose_name = _('Campaign')
        verbose_name_plural = _('Campaigns')

    def __unicode__(self):
        return self.display_name or self.subject

    def get_absolute_url(self):
        return reverse('mailchimp_campaign_detail', kwargs={'pk': self.pk, 'slug': self.slug})


class CampaignArchivePlugin(CMSPlugin):
    count = models.PositiveSmallIntegerField(
        _('count'), null=True, blank=True, help_text=_('Leave blank to display all')
    )
    categories = models.ManyToManyField(
        Category, verbose_name=_('filter by category/categories'), blank=True, null=True
    )

    def copy_relations(self, old_instance):
        self.categories = old_instance.categories.all()


class SelectedCampaignsPlugin(CMSPlugin):
    campaigns = models.ManyToManyField(Campaign)

    def copy_relations(self, old_instance):
        self.campaigns = old_instance.campaigns.all()
