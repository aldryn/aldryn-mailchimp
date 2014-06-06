# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class SubscriptionPlugin(CMSPlugin):

    list_id = models.CharField(_('List ID'), max_length=20)
    assign_language = models.BooleanField(
        _('Save user\'s language'), default=True,help_text=_('Save the user\'s language based on the page language'))

    def __unicode__(self):
        return str(self.list_id)
