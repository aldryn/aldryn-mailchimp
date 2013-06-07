# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class SubscriptionPlugin(CMSPlugin):

    list_id = models.PositiveIntegerField(_('List ID'))

    def __unicode__(self):
        return str(self.list_id)
