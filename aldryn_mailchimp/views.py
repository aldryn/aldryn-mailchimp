# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView

from aldryn_mailchimp.forms import SubscriptionForm


class SubscriptionView(FormView):

    form_class = SubscriptionForm
    template_name = 'aldryn_mailchimp/subscription.html'

    def form_valid(self, form):
        messages.success(self.request, _(u'Successfully subscribed for mailing list.'))
        return redirect(form.cleaned_data['redirect_url'])
