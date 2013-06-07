# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView

import mailchimp

from aldryn_mailchimp.forms import SubscriptionForm


class SubscriptionView(FormView):

    form_class = SubscriptionForm
    template_name = 'aldryn_mailchimp/subscription.html'

    def form_valid(self, form):
        mailchimp_client = mailchimp.MailChimp(settings.MAILCHIMP_API_KEY)
        try:
            mailchimp_client.listSubscribe(id=form.cleaned_data['list_id'], email_address=form.cleaned_data['email'])
        except Exception, e:
            messages.error(self.request, e.error)
        else:
            messages.success(self.request, _(u'Successfully subscribed for mailing list.'))
        return redirect(form.cleaned_data['redirect_url'])
