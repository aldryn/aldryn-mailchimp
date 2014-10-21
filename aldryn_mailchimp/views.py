# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.generic import FormView, DetailView

from pyrate.services import mailchimp

from .utils import get_language_for_code
from .forms import SubscriptionPluginForm
from .models import SubscriptionPlugin, Campaign


ERROR_MESSAGES = {
    104: _('Invalid API-Key'),
    200: _('The selected list does not exist.'),
    214: _('You are already subscribed to our list.'),
    230: _('You are already subscribed to our list.'),
}


class SubscriptionView(FormView):

    form_class = SubscriptionPluginForm
    template_name = 'aldryn_mailchimp/subscription.html'

    def form_valid(self, form):
        h = mailchimp.MailchimpPyrate(settings.MAILCHIMP_API_KEY)
        plugin = get_object_or_404(SubscriptionPlugin, pk=form.cleaned_data['plugin_id'])

        merge_vars = None
        if plugin.assign_language:
            language = get_language_for_code(self.request.LANGUAGE_CODE)
            if language:
                merge_vars = {'mc_language': language}

        try:
            h.subscribe_to_list(list_id=plugin.list_id, user_email=form.cleaned_data['email'], merge_vars=merge_vars)
        except Exception as exc:
            try:
                message = ERROR_MESSAGES[exc.code]
            except (AttributeError, KeyError):
                message = ugettext(u'Oops, something must have gone wrong. Please try again later.')

            if self.request.user.is_superuser and hasattr(exc, 'code'):
                message = u'%s (MailChimp Error (%s): %s)'% (message, exc.code, exc)

            messages.error(self.request, message)
        else:
            messages.success(self.request, ugettext(u'You have successfully subscribed to our mailing list.'))
        return redirect(form.cleaned_data['redirect_url'])

    def form_invalid(self, form):
        redirect_url = form.data.get('redirect_url')

        if redirect_url:
            message = _(u'Please enter a valid email.')
            messages.error(self.request, message)
            response = HttpResponseRedirect(redirect_url)
        else:
            # user has tampered with the redirect_url field.
            response = HttpResponseBadRequest()
        return response


class CampaignDetail(DetailView):
    model = Campaign

    @property
    def template_name_suffix(self):
        default = '_detail'
        iframe = '_detail_iframe'
        return iframe if 'iframe' in self.request.GET else default

    def get_queryset(self):
        return self.model.objects.published()

campaign_detail = CampaignDetail.as_view()
