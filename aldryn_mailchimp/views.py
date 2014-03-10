# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView

import mailchimp

from aldryn_mailchimp.forms import SubscriptionForm
from aldryn_mailchimp.models import SubscriptionPlugin


class SubscriptionView(FormView):

    form_class = SubscriptionForm
    template_name = 'aldryn_mailchimp/subscription.html'

    def form_valid(self, form):
        mailchimp_client = mailchimp.MailChimp(settings.MAILCHIMP_API_KEY)
        plugin = get_object_or_404(SubscriptionPlugin, pk=form.cleaned_data['plugin_id'])
        try:
            mailchimp_client.listSubscribe(id=plugin.list_id, email_address=form.cleaned_data['email'])
        except Exception, e:
            messages.error(self.request, _(u'Oops, something must have gone wrong. Please try again later.'))
        else:
            messages.success(self.request, _(u'Successfully subscribed for mailing list.'))
        return redirect(form.cleaned_data['redirect_url'])
